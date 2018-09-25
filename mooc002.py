#P301

#读取HTML文件内容
def getHTMLlines(htmlpath):
    f = open(htmlpath,"r",encoding = 'utf-8')
    ls = f.readlines()
    f.close()
    return ls

#用于解析文件并提取图像的URL
def extractImageUrls(htmllist):
    urls = []
    for line in htmllist:
        if 'img' in line:
            url = line.split('src=')[-1].split('"')[1]
            if 'http' in url:
                urls.append(url)
    return urls

#将获取的链接输出到屏幕上
def showResults(urls):
    count = 1
    for url in urls:
        print("第{:2}个URL:{}".format(count,url))
        count += 1

# 主程序：1 读取文件；2 解析并提取其中的图片链接；3 输出提取结果到屏幕
def main():
    inputfile = "ngchina.html"
    htmllines = getHTMLlines(inputfile)
    imageUrls = extractImageUrls(htmllines)
    showResults(imageUrls)
    
main()
