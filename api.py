import requests
import json
import xml.etree.ElementTree as ET

# API 網址 (回傳 XML)
url = "https://api.nlsc.gov.tw/idc/TextQueryRoad/H/遠東"

def fetch_data():
    try:
        response = requests.get(url)
        response.raise_for_status()

        response.encoding = 'utf-8'
        xml_data = response.text

        # 解析 XML
        root = ET.fromstring(xml_data)

        data_list = []

        # 假設 root 底下每個子節點就是一筆資料
        for record in root:
            record_dict = {}

            for child in record:
                if child.text and child.text.strip():
                    record_dict[child.tag] = child.text.strip()

            if record_dict:
                data_list.append(record_dict)

        # 儲存成 JSON
        with open("road_data.json", "w", encoding="utf-8") as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)

        print("XML 資料已成功轉換並儲存至 road_data.json")

    except Exception as e:
        print(f"發生錯誤：{e}")

if __name__ == "__main__":
    fetch_data()
