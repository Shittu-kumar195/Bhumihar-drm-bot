import logging
import subprocess
import asyncio
import os
import time, shutil
import subprocess
from Cryptodome.Cipher import AES
import base64
from Cryptodome.Util.Padding import unpad
from subprocess import getstatusoutput

def decrypt_encrypted_mpd_key(url):
    key = b'638udh3829162018'
    iv = b'fedcba9876543210'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = base64.b64decode(url.encode('utf-8'))
    decrypted_data = cipher.decrypt(ciphertext)
    decrypted_data = unpad(decrypted_data, AES.block_size)
    mpd, keys = decrypted_data.decode().split(" * ")
    return mpd, keys

def duration(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

async def download_video(url, cmd, name):
    download_cmd = f'{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args "aria2c: -x 16 -j 32"'
    global failed_counter
    print(download_cmd)
    logging.info(download_cmd)
    k = subprocess.run(download_cmd, shell=True)
    if "visionias" in cmd and k.returncode != 0 and failed_counter <= 10:
        failed_counter += 1
        await asyncio.sleep(5)
        await download_video(url, cmd, name)
    failed_counter = 0
    try:
        if os.path.isfile(name):
            return name
        elif os.path.isfile(f"{name}.webm"):
            return f"{name}.webm"
        name = name.split(".")[0]
        if os.path.isfile(f"{name}.mkv"):
            return f"{name}.mkv"
        elif os.path.isfile(f"{name}.mp4"):
            return f"{name}.mp4"
        elif os.path.isfile(f"{name}.mp4.webm"):
            return f"{name}.mp4.webm"

        return name
    except FileNotFoundError as esc:
        return os.path.isfile.splitext[0] + "." + "mp4"
    
    
async def send_vid(bot, m, cc, filename, thumb, name, prog, url, channel_id):
    xx = await bot.send_message(channel_id, f"**Generate Thumbnail** - `{name}`")
    await prog.delete(True)
    await xx.delete()  
    reply = await bot.send_message(channel_id, f"**📩 Uploading 📩:-**\n\n**Name :-** `{name}\n🎥**Url -** `{url}`\n\nDRM Bot Made By 🔰『@NtrRazYt』🔰") 
    try:
        if thumb.startswith("http://") or thumb.startswith("https://"):
            getstatusoutput(f"wget '{thumb}' -O 'Local_thumb.jpg'")
            thumb = "Local_thumb.jpg"
            logging.info("Url Thumb downloaded successfully!")
        elif thumb.lower() == "no":
            subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
            subprocess.run(f'ffmpeg -i "{filename}.jpg" -i watermark.png -filter_complex "overlay=(W-w)/2:(H-h)/2" "{filename}_thumbnail_watermarked.jpg"', shell=True)
            thumb = f"{filename}_thumbnail_watermarked.jpg"
            logging.info("Watermark Thumb downloaded successfully!")
        else:
            subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
            thumb = f"{filename}.jpg"
            logging.info("Default Thumb downloaded successfully!")
    except Exception as e:
        logging.error(f"Error while processing thumbnail: {e}")
        await m.reply_text(str(e))  
    dur = int(duration(filename))
    start_time = time.time()   
    try:
        await bot.send_video(chat_id=channel_id, video=filename, caption=cc, supports_streaming=True, height=720, width=1280, thumb=thumb, duration=dur, progress_args=(reply, start_time))
    except Exception as e:
        logging.error(f"Error while sending video: {e}")
        await bot.send_video(chat_id=channel_id, video=filename, caption=cc, progress_args=(reply, start_time))   
    os.remove(filename)
    if thumb.endswith("_thumbnail_watermarked.jpg"):
        os.remove(f"{filename}.jpg")
        os.remove(thumb)
    elif thumb == "Local_thumb.jpg":
        os.remove(thumb)
    elif thumb.endswith(".jpg"):
        os.remove(thumb)
    await reply.delete(True)



async def download_and_dec_video(mpd, keys, path, name, raw_text2):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    subprocess.run(f'yt-dlp -o "{path}/fileName.%(ext)s" -f "bestvideo[height<={int(raw_text2)}]+bestaudio" --allow-unplayable-format --external-downloader aria2c "{mpd}"', shell=True)
    avDir = os.listdir(path)
    print(avDir)
    print("Decrypting")
    try:
        for data in avDir:
            if data.endswith("mp4"):
                cmd2 = f'mp4decrypt {keys} --show-progress "{path}/{data}" "{path}/video.mp4"'
                subprocess.run(cmd2, shell=True)
                os.remove(f'{path}/{data}')
                print('Video Dec done')
            elif data.endswith("m4a"):
                cmd3 = f'mp4decrypt {keys} --show-progress "{path}/{data}" "{path}/audio.m4a"'
                subprocess.run(cmd3, shell=True)
                os.remove(f'{path}/{data}')
                print("audio dec done")
    except FileNotFoundError:
        return os.path.splitext(name)[0] + "." + "mp4"

async def merge_and_send_vid(bot, m, cc, name, prog, path, url, thumb, channel_id):
    xx = await bot.send_message(channel_id, f"**Video & Audio Merging** - `{name}`")
    video_path = os.path.join(path, "video.mp4")  
    audio_path = os.path.join(path, "audio.m4a") 
    subprocess.run(f'ffmpeg -i "{video_path}" -i "{audio_path}" -c copy "{os.path.join(path, name)}.mp4"', shell=True)
    os.remove(video_path)
    os.remove(audio_path)
    video = f"{os.path.join(path, name)}.mp4"
    await xx.edit("Generate Thumbnail")
    await prog.delete(True)
    await xx.delete()  
    reply = await bot.send_message(channel_id, f"**📩 Uploading 📩:-**\n\n**Name :-** `{name}\n🎥**Url -** `{url}`\n\nDRM Bot Made By 🔰『@NtrRazYt』🔰") 
    try:
        if thumb.startswith("http://") or thumb.startswith("https://"):
            getstatusoutput(f"wget '{thumb}' -O 'Local_thumb.jpg'")
            thumb = "Local_thumb.jpg"
            logging.info("Url Thumb downloaded successfully!")
        elif thumb.lower() == "no":
            subprocess.run(f'ffmpeg -i "{video}" -ss 00:01:00 -vframes 1 "{video}.jpg"', shell=True)
            subprocess.run(f'ffmpeg -i "{video}.jpg" -i watermark.png -filter_complex "overlay=(W-w)/2:(H-h)/2" "{video}_thumbnail_watermarked.jpg"', shell=True)
            thumb = f"{video}_thumbnail_watermarked.jpg"
            logging.info("Watermark Thumb downloaded successfully!")
        else:
            subprocess.run(f'ffmpeg -i "{video}" -ss 00:01:00 -vframes 1 "{video}.jpg"', shell=True)
            thumb = f"{video}.jpg"
            logging.info("Default Thumb downloaded successfully!")
    except Exception as e:
        logging.error(f"Error while processing thumbnail: {e}")
        await m.reply_text(str(e))  
    dur = int(duration(video))
    start_time = time.time() 
    try:  
        await bot.send_video(chat_id=channel_id, video=video, thumb=thumb, caption=cc, supports_streaming=True, height=720, width=1280, duration=dur, progress_args=(reply, start_time))  
    except Exception as e:
        logging.error(f"Error while sending video: {e}")
        await bot.send_video(chat_id=channel_id, video=video, caption=cc, progress_args=(reply, start_time))   
    os.remove(video)
    if thumb.endswith("_thumbnail_watermarked.jpg"):
        os.remove(f"{video}.jpg")
        os.remove(thumb)
    elif thumb == "Local_thumb.jpg":
        os.remove(thumb)
    elif thumb.endswith(".jpg"):
        os.remove(thumb)
    await reply.delete(True)


def duration(video):
    try:
        result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", video], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return float(result.stdout)
    except Exception:
        return 0
