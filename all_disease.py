import requests
import json

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    url = 'http://code.nhsa.gov.cn:8000/jbzd/public/toStdIcdTreeList.html'
    all_chapter_list = requests.post(url=url, headers=headers).json()

    chapter_ids = []
    section_ids = []
    detail_ids = []
    all_section_list = []
    all_detail_list = []
    all_last_list = []
    # 第几章
    for chapter_dic in all_chapter_list:
        # 获取章节的ID并加入到chapter_ids里面
        chapter_ids.append(chapter_dic["icdId"])
    # print(chapter_ids)  # 打印所有章的ID
    # 根据章节的ID去寻找第二级目录的ID
    for section_icdId in chapter_ids:
        data = {
            'icdId': section_icdId
        }
        section_list = requests.post(url=url, headers=headers, data=data).json()
        all_section_list.append(section_list)

    for i in range(0, len(chapter_ids)):
        all_detail_list = all_section_list[i]
        for detail_dic in all_detail_list:
            detail_ids.append(detail_dic["icdId"])
    for last_icdId in detail_ids:
        data = {
            'icdId': last_icdId
        }
        last_list = requests.post(url=url, headers=headers, data=data).json()
        all_last_list.append(last_list)
    fp = open('./disease.json', 'w', encoding='utf-8')
    json.dump(all_last_list, fp=fp, ensure_ascii=False)
    print("Success!!!")
