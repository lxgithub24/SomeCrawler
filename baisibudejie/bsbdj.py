# -*- coding: utf-8 -*-
import requests
import videos
from videos import Videos
from common import (
    WebVideo,
    get_md5,
)
from pyquery import PyQuery


def get_bsbdj():
    url = "http://www.budejie.com/new-video/"
    name = 'budejie-1'
    v_list = extract_videos(url, name)

def extract_videos(url,name):
    source,task_id = name.split('-')
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
    }
    response = requests.get(url, timeout=10, headers=headers)
    videos = get_video_lists(response.content, source, int(task_id))
    new_videos = Videos.filter_exist(videos)
    Videos.batch_add(new_videos)
    print videos
    return videos

def get_video_lists(html, source, task_id):
    page = PyQuery(html)
    result = []
    for item in page("div[class=j-r-list]").children("ul").children("li").items():
        title = item("div[class='j-r-list-c-desc']").text()
        img_url = item("div[class=' j-video']").attr("data-poster")
        video_url = 'http://www.budejie.com{}'.format(
            item("div[class='j-r-list-c-desc'] a").attr("href")
        )

        result.append(WebVideo(
            source=source,
            task_id=task_id,
            img_url=img_url,
            duration=0,
            title=title,
            video_url=video_url,
            video_url_md5=get_md5(video_url)
        ))

    return result

if __name__ == '__main__':
    get_bsbdj()