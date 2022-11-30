"""

    • On the first line, you will receive a title of an article
    • On the second line, you will receive the content of that article
    • On the following lines, until you receive "end of comments" you will
        get the comments about the article

Print the whole information in html format:
    • The title should be in "h1" tag (<h1></h1>)
    • The content in article tag (<article></article>)
    • Each comment should be in div tag (<div></div>)

"""

title = input()
print(f"<h1>\n    {title}\n</h1>")
content = input()
print(f"<article>\n    {content}\n</article>")
while True:
    comments = input()
    if comments == 'end of comments':
        break
    else:
        print(f"<div>\n    {comments}\n</div>")
