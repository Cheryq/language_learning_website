# 导入seleinum webdriver接口
from selenium import webdriver
from lxml import etree
import time
# 创建Chrome浏览器对象
browser = webdriver.Chrome()
#访问百度网站
browser.get('https://mandarincompanion.com/blog/')
#阻塞3秒
time.sleep(5)
browser.execute_script(
      'window.scrollTo(0,document.body.scrollHeight)'#拉动进度条至底部
)
time.sleep(8)
browser.execute_script(
      'window.scrollTo(0,document.body.scrollHeight)'#拉动进度条至底部
)
time.sleep(8)
browser.execute_script(
      'window.scrollTo(0,document.body.scrollHeight)'#拉动进度条至底部
)
time.sleep(8)
browser.execute_script(
      'window.scrollTo(0,document.body.scrollHeight)'#拉动进度条至底部
)
time.sleep(8)
source=browser.page_source
print(source.encode("utf8"))
print(type(source))
tree=etree.HTML(source)
res=tree.xpath('//a[@class="sc_button sc_button_square sc_button_style_filled sc_button_bg_link sc_button_size_small"]/@href')
print(res)
print(len(res))
list=['https://mandarincompanion.com/blog/improve-your-listening-skills-step-1-know-the-challenges/', 'https://mandarincompanion.com/blog/how-to-read-chinese-in-4-steps-a-guide-for-beginners/', 'https://mandarincompanion.com/blog/chinese-reading-exercises/', 'https://mandarincompanion.com/blog/chinese-tutor/', 'https://mandarincompanion.com/blog/teach-yourself-mandarin/', 'https://mandarincompanion.com/blog/motivation-to-learn-chinese/', 'https://mandarincompanion.com/blog/chinese-reading-for-beginners/', 'https://mandarincompanion.com/blog/new-book-just-friends-breakthrough-level/', 'https://mandarincompanion.com/blog/new-breakthrough-story-in-search-of-hua-ma/', 'https://mandarincompanion.com/blog/new-breakthrough-story-my-teacher-is-a-martian/', 'https://mandarincompanion.com/blog/interview-with-steven-kaufmann-the-linguist/', 'https://mandarincompanion.com/blog/audiobooks-are-here/', 'https://mandarincompanion.com/blog/launch-of-the-new-breakthrough-level-books-150-characters/', 'https://mandarincompanion.com/blog/how-to-pass-the-ap-chinese-exam-secrets-from-a-teacher-with-a-perfect-pass-rate/', 'https://mandarincompanion.com/blog/stories-from-our-readers-from-flash-cards-to-martial-arts-jonathans-story/', 'https://mandarincompanion.com/blog/announcing-the-launch-of-our-podcast/', 'https://mandarincompanion.com/blog/mandarin-companion-preview-for-2019/', 'https://mandarincompanion.com/blog/emma-the-prince-and-the-pauper-and-the-ransom-of-red-chief-now-available-on-kindle/', 'https://mandarincompanion.com/blog/stories-from-our-readers-i-couldnt-believe-i-could-read-harriets-story/', 'https://mandarincompanion.com/blog/what-if-beginning-level-chinese-books-are-too-hard-10-tips-for-beginning-readers/', 'https://mandarincompanion.com/blog/stories-from-our-readers-chinese-is-like-an-elephant/', 'https://mandarincompanion.com/blog/why-we-forget/', 'https://mandarincompanion.com/blog/pinyin-over-characters-the-crippling-crutch/', 'https://mandarincompanion.com/blog/dont-be-so-serious-finally-a-funny-level-1-story/', 'https://mandarincompanion.com/blog/independent-study-confirms-the-readability-of-the-mandarin-companion-series/', 'https://mandarincompanion.com/blog/confessions-of-a-chinese-immigrant/', 'https://mandarincompanion.com/blog/jane-austens-emma/', 'https://mandarincompanion.com/blog/new-cooperation-between-chinesepod-and-mandarin-companion/', 'https://mandarincompanion.com/blog/the-prince-and-the-pauper-level-1-graded-reader/', 'https://mandarincompanion.com/blog/all-traditional-character-editions-available-in-paperback/', 'https://mandarincompanion.com/blog/journey-to-the-center-of-the-earth-illustration-adaptations/', 'https://mandarincompanion.com/blog/level-2-traditional-chinese-character-editions-on-sale/', 'https://mandarincompanion.com/blog/mandarin-companion-word-lists-now-available/', 'https://mandarincompanion.com/blog/the-magic-of-learning-from-context/', 'https://mandarincompanion.com/blog/level-2-is-here/', 'https://mandarincompanion.com/blog/will-reading-chinese-poems-improve-my-chinese/', 'https://mandarincompanion.com/blog/mandarin-companion-series-now-available-in-paperback/', 'https://mandarincompanion.com/blog/how-to-fix-your-e-reader-chinese-font-display-problems/', 'https://mandarincompanion.com/blog/the-secret-garden-in-paperback-and-level-2-update/', 'https://mandarincompanion.com/blog/how-great-are-your-expectations-level-2-in-progress/', 'https://mandarincompanion.com/blog/i-cant-learn-chinese-its-too-hard/', 'https://mandarincompanion.com/blog/the-impact-of-reading-results-of-a-40-year-study/', 'https://mandarincompanion.com/blog/the-only-way-we-truly-acquire-a-language/', 'https://mandarincompanion.com/blog/the-vicious-cycle-of-the-poor-reader/', 'https://mandarincompanion.com/blog/is-this-book-a-graded-reade/', 'https://mandarincompanion.com/blog/elementary-my-dear-watson-how-we-adapted-a-classic-to-chinese/', 'https://mandarincompanion.com/blog/activities-to-get-the-most-out-of-your-books/', 'https://mandarincompanion.com/blog/7-mistakes-about-extensive-reading/', 'https://mandarincompanion.com/blog/tales-from-readers-the-most-interesting-man-in-the-world/', 'https://mandarincompanion.com/blog/mandarin-companion-now-on-skritter/', 'https://mandarincompanion.com/blog/the-monkeys-paw-how-gruesome-should-it-be/', 'https://mandarincompanion.com/blog/reading-pain-or-reading-gain-reading-at-the-right-level/', 'https://mandarincompanion.com/blog/how-reading-in-chinese-changed-my-life/', 'https://mandarincompanion.com/blog/fateful-beginnings/', 'https://mandarincompanion.com/blog/welcome-to-mandarin-companion/']

