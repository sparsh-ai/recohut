"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[48387],{3905:(e,n,t)=>{t.d(n,{Zo:()=>l,kt:()=>g});var r=t(67294);function a(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function i(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function s(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?i(Object(t),!0).forEach((function(n){a(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):i(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function o(e,n){if(null==e)return{};var t,r,a=function(e,n){if(null==e)return{};var t,r,a={},i=Object.keys(e);for(r=0;r<i.length;r++)t=i[r],n.indexOf(t)>=0||(a[t]=e[t]);return a}(e,n);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)t=i[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(a[t]=e[t])}return a}var p=r.createContext({}),c=function(e){var n=r.useContext(p),t=n;return e&&(t="function"==typeof e?e(n):s(s({},n),e)),t},l=function(e){var n=c(e.components);return r.createElement(p.Provider,{value:n},e.children)},m={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},u=r.forwardRef((function(e,n){var t=e.components,a=e.mdxType,i=e.originalType,p=e.parentName,l=o(e,["components","mdxType","originalType","parentName"]),u=c(t),g=a,y=u["".concat(p,".").concat(g)]||u[g]||m[g]||i;return t?r.createElement(y,s(s({ref:n},l),{},{components:t})):r.createElement(y,s({ref:n},l))}));function g(e,n){var t=arguments,a=n&&n.mdxType;if("string"==typeof e||a){var i=t.length,s=new Array(i);s[0]=u;var o={};for(var p in n)hasOwnProperty.call(n,p)&&(o[p]=n[p]);o.originalType=e,o.mdxType="string"==typeof e?e:a,s[1]=o;for(var c=2;c<i;c++)s[c]=t[c];return r.createElement.apply(null,s)}return r.createElement.apply(null,t)}u.displayName="MDXCreateElement"},971:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>p,contentTitle:()=>s,default:()=>m,frontMatter:()=>i,metadata:()=>o,toc:()=>c});var r=t(87462),a=(t(67294),t(3905));const i={title:"Web Scraping using Scrapy, BS4, and Selenium",authors:"sparsh",tags:["scraping"]},s=void 0,o={permalink:"/blog/2021/10/01/web-scraping-using-scrapy-bs4-and-selenium",source:"@site/blog/2021-10-01-web-scraping-using-scrapy-bs4-and-selenium.mdx",title:"Web Scraping using Scrapy, BS4, and Selenium",description:"1. Handling single request & response by extracting a city\u2019s weather from a weather site using Scrapy",date:"2021-10-01T00:00:00.000Z",formattedDate:"October 1, 2021",tags:[{label:"scraping",permalink:"/blog/tags/scraping"}],readingTime:3.78,hasTruncateMarker:!1,authors:[{name:"Sparsh Agarwal",title:"Data Scientist & Engineer",url:"https://github.com/sparsh-ai",email:"sprsag@gmail.com",imageURL:"https://github.com/sparsh-ai.png",key:"sparsh"}],frontMatter:{title:"Web Scraping using Scrapy, BS4, and Selenium",authors:"sparsh",tags:["scraping"]},prevItem:{title:"Vehicle Suggestions",permalink:"/blog/2021/10/01/vehicle-suggestions"},nextItem:{title:"Web Scraping with Gazpacho",permalink:"/blog/2021/10/01/web-scraping-with-gazpacho"}},p={authorsImageUrls:[void 0]},c=[{value:"Project tree",id:"project-tree",level:2}],l={toc:c};function m(e){let{components:n,...i}=e;return(0,a.kt)("wrapper",(0,r.Z)({},l,i,{components:n,mdxType:"MDXLayout"}),(0,a.kt)("ol",null,(0,a.kt)("li",{parentName:"ol"},"Handling single request & response by extracting a city\u2019s weather from a weather site using Scrapy"),(0,a.kt)("li",{parentName:"ol"},"Handling multiple request & response by extracting book details from a dummy online book store using Scrapy"),(0,a.kt)("li",{parentName:"ol"},"Scrape the cover images of all the books from the website ",(0,a.kt)("a",{parentName:"li",href:"http://books.toscrape.com/"},"books.toscrape.com")," using Scrapy"),(0,a.kt)("li",{parentName:"ol"},"Logging into Facebook using Selenium"),(0,a.kt)("li",{parentName:"ol"},"Extract PM2.5 data from ",(0,a.kt)("a",{parentName:"li",href:"http://openaq.org"},"openaq.org")," using Selenium"),(0,a.kt)("li",{parentName:"ol"},"Extract PM2.5 data from ",(0,a.kt)("a",{parentName:"li",href:"http://openaq.org"},"openaq.org")," using Selenium Scrapy")),(0,a.kt)("admonition",{title:"Scrapy vs. Selenium",type:"note"},(0,a.kt)("p",{parentName:"admonition"},"Selenium is an automation tool for testing web applications. It uses a webdriver as an interface to control webpages through programming languages. So, this gives Selenium the capability to handle dynamic webpages effectively. Selenium is capable of extracting data on its own. It is true, but it has its caveats. Selenium cannot handle large data, but Scrapy can handle large data with ease. Also, Selenium is much slower when compared to Scrapy. So, the smart choice would be to use Selenium with Scrapy to scrape dynamic webpages containing large data, consuming less time. Combining Selenium with Scrapy is a simpler process. All that needs to be done is let Selenium render the webpage and once it is done, pass the webpage\u2019s source to create a Scrapy Selector object. And from here on, Scrapy can crawl the page with ease and effectively extract a large amount of data.")),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},"# SKELETON FOR COMBINING SELENIUM WITH SCRAPY\nfrom scrapy import Selector\n# Other Selenium and Scrapy imports\n...\ndriver = webdriver.Chrome()\n# Selenium tasks and actions to render the webpage with required content\nselenium_response_text = driver.page_source\nnew_selector = Selector(text=selenium_response_text)\n# Scrapy tasks to extract data from Selector\n")),(0,a.kt)("h2",{id:"project-tree"},"Project tree"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-html"},".\n\u251c\u2500\u2500 airQuality\n\u2502   \u251c\u2500\u2500 countries_list.json\n\u2502   \u251c\u2500\u2500 get_countries.py\n\u2502   \u251c\u2500\u2500 get_pm_data.py\n\u2502   \u251c\u2500\u2500 get_urls.py\n\u2502   \u251c\u2500\u2500 openaq_data.json\n\u2502   \u251c\u2500\u2500 openaq_scraper.py\n\u2502   \u251c\u2500\u2500 README.md\n\u2502   \u2514\u2500\u2500 urls.json\n\u251c\u2500\u2500 airQualityScrapy\n\u2502   \u251c\u2500\u2500 LICENSE\n\u2502   \u251c\u2500\u2500 openaq\n\u2502   \u2502   \u251c\u2500\u2500 countries_list.json\n\u2502   \u2502   \u251c\u2500\u2500 openaq\n\u2502   \u2502   \u2502   \u251c\u2500\u2500 __init__.py\n\u2502   \u2502   \u2502   \u251c\u2500\u2500 items.py\n\u2502   \u2502   \u2502   \u251c\u2500\u2500 middlewares.py\n\u2502   \u2502   \u2502   \u251c\u2500\u2500 pipelines.py\n\u2502   \u2502   \u2502   \u251c\u2500\u2500 settings.py\n\u2502   \u2502   \u2502   \u2514\u2500\u2500 spiders\n\u2502   \u2502   \u251c\u2500\u2500 output.json\n\u2502   \u2502   \u251c\u2500\u2500 README.md\n\u2502   \u2502   \u251c\u2500\u2500 scrapy.cfg\n\u2502   \u2502   \u2514\u2500\u2500 urls.json\n\u2502   \u251c\u2500\u2500 performance_comparison\n\u2502   \u2502   \u251c\u2500\u2500 performance_comparison\n\u2502   \u2502   \u2502   \u251c\u2500\u2500 __init__.py\n\u2502   \u2502   \u2502   \u251c\u2500\u2500 items.py\n\u2502   \u2502   \u2502   \u251c\u2500\u2500 middlewares.py\n\u2502   \u2502   \u2502   \u251c\u2500\u2500 pipelines.py\n\u2502   \u2502   \u2502   \u251c\u2500\u2500 settings.py\n\u2502   \u2502   \u2502   \u2514\u2500\u2500 spiders\n\u2502   \u2502   \u251c\u2500\u2500 README.md\n\u2502   \u2502   \u251c\u2500\u2500 scrapy.cfg\n\u2502   \u2502   \u251c\u2500\u2500 scrapy_output.json\n\u2502   \u2502   \u2514\u2500\u2500 selenium_scraper\n\u2502   \u2502       \u251c\u2500\u2500 bts_scraper.py\n\u2502   \u2502       \u251c\u2500\u2500 selenium_output.json\n\u2502   \u2502       \u2514\u2500\u2500 urls.json\n\u2502   \u2514\u2500\u2500 README.md\n\u251c\u2500\u2500 books\n\u2502   \u251c\u2500\u2500 books\n\u2502   \u2502   \u251c\u2500\u2500 __init__.py\n\u2502   \u2502   \u251c\u2500\u2500 items.py\n\u2502   \u2502   \u251c\u2500\u2500 middlewares.py\n\u2502   \u2502   \u251c\u2500\u2500 pipelines.py\n\u2502   \u2502   \u251c\u2500\u2500 settings.py\n\u2502   \u2502   \u2514\u2500\u2500 spiders\n\u2502   \u2502       \u251c\u2500\u2500 book_spider.py\n\u2502   \u2502       \u251c\u2500\u2500 crawl_spider.py\n\u2502   \u2502       \u2514\u2500\u2500 __init__.py\n\u2502   \u251c\u2500\u2500 crawl_spider_output.json\n\u2502   \u251c\u2500\u2500 README.md\n\u2502   \u2514\u2500\u2500 scrapy.cfg\n\u251c\u2500\u2500 booksCoverImage\n\u2502   \u251c\u2500\u2500 booksCoverImage\n\u2502   \u2502   \u251c\u2500\u2500 __init__.py\n\u2502   \u2502   \u251c\u2500\u2500 items.py\n\u2502   \u2502   \u251c\u2500\u2500 middlewares.py\n\u2502   \u2502   \u251c\u2500\u2500 pipelines.py\n\u2502   \u2502   \u251c\u2500\u2500 settings.py\n\u2502   \u2502   \u2514\u2500\u2500 spiders\n\u2502   \u2502       \u251c\u2500\u2500 image_crawl_spider.py\n\u2502   \u2502       \u2514\u2500\u2500 __init__.py\n\u2502   \u251c\u2500\u2500 output.json\n\u2502   \u251c\u2500\u2500 path\n\u2502   \u2502   \u2514\u2500\u2500 to\n\u2502   \u2502       \u2514\u2500\u2500 store\n\u2502   \u251c\u2500\u2500 README.md\n\u2502   \u2514\u2500\u2500 scrapy.cfg\n\u251c\u2500\u2500 etc\n\u2502   \u2514\u2500\u2500 Selenium\n\u2502       \u251c\u2500\u2500 chromedriver.exe\n\u2502       \u251c\u2500\u2500 chromedriver_v87.exe\n\u2502       \u2514\u2500\u2500 install.sh\n\u251c\u2500\u2500 facebook\n\u2502   \u2514\u2500\u2500 login.py\n\u251c\u2500\u2500 gazpacho1\n\u2502   \u251c\u2500\u2500 data\n\u2502   \u2502   \u251c\u2500\u2500 media.html\n\u2502   \u2502   \u251c\u2500\u2500 ocr.html\n\u2502   \u2502   \u251c\u2500\u2500 page.html\n\u2502   \u2502   \u251c\u2500\u2500 static\n\u2502   \u2502   \u2502   \u2514\u2500\u2500 stheno.mp4\n\u2502   \u2502   \u2514\u2500\u2500 table.html\n\u2502   \u251c\u2500\u2500 media\n\u2502   \u2502   \u251c\u2500\u2500 euryale.png\n\u2502   \u2502   \u251c\u2500\u2500 medusa.mp3\n\u2502   \u2502   \u251c\u2500\u2500 medusa.png\n\u2502   \u2502   \u251c\u2500\u2500 stheno.mp4\n\u2502   \u2502   \u2514\u2500\u2500 test.png\n\u2502   \u251c\u2500\u2500 scrap_login.py\n\u2502   \u251c\u2500\u2500 scrap_media.py\n\u2502   \u251c\u2500\u2500 scrap_ocr.py\n\u2502   \u251c\u2500\u2500 scrap_page.py\n\u2502   \u2514\u2500\u2500 scrap_table.py\n\u251c\u2500\u2500 houzzdotcom\n\u2502   \u251c\u2500\u2500 houzzdotcom\n\u2502   \u2502   \u251c\u2500\u2500 __init__.py\n\u2502   \u2502   \u251c\u2500\u2500 items.py\n\u2502   \u2502   \u251c\u2500\u2500 middlewares.py\n\u2502   \u2502   \u251c\u2500\u2500 pipelines.py\n\u2502   \u2502   \u251c\u2500\u2500 settings.py\n\u2502   \u2502   \u2514\u2500\u2500 spiders\n\u2502   \u2502       \u251c\u2500\u2500 crawl_spider.py\n\u2502   \u2502       \u2514\u2500\u2500 __init__.py\n\u2502   \u2514\u2500\u2500 scrapy.cfg\n\u251c\u2500\u2500 media\n\u2502   \u2514\u2500\u2500 test.png\n\u251c\u2500\u2500 README.md\n\u251c\u2500\u2500 scrapyPractice\n\u2502   \u251c\u2500\u2500 scrapy.cfg\n\u2502   \u2514\u2500\u2500 scrapyPractice\n\u2502       \u251c\u2500\u2500 __init__.py\n\u2502       \u251c\u2500\u2500 items.py\n\u2502       \u251c\u2500\u2500 middlewares.py\n\u2502       \u251c\u2500\u2500 pipelines.py\n\u2502       \u251c\u2500\u2500 settings.py\n\u2502       \u2514\u2500\u2500 spiders\n\u2502           \u2514\u2500\u2500 __init__.py\n\u2514\u2500\u2500 weather\n    \u251c\u2500\u2500 output.json\n    \u251c\u2500\u2500 README.md\n    \u251c\u2500\u2500 scrapy.cfg\n    \u2514\u2500\u2500 weather\n        \u251c\u2500\u2500 __init__.py\n        \u251c\u2500\u2500 items.py\n        \u251c\u2500\u2500 middlewares.py\n        \u251c\u2500\u2500 pipelines.py\n        \u251c\u2500\u2500 settings.py\n        \u2514\u2500\u2500 spiders\n            \u251c\u2500\u2500 __init__.py\n            \u2514\u2500\u2500 weather_spider.py\n\n35 directories, 98 files\n")),(0,a.kt)("p",null,(0,a.kt)("img",{alt:"For code, drop me a message on mail or LinkedIn.",src:t(47213).Z,width:"1292",height:"619"})),(0,a.kt)("p",null,"For code, drop me a message on mail or LinkedIn."))}m.isMDXComponent=!0},47213:(e,n,t)=>{t.d(n,{Z:()=>r});const r=t.p+"assets/images/content-blog-raw-blog-web-scraping-using-scrapy-bs4-and-selenium-untitled-f6a60dc9084f918baca047c531a5849e.png"}}]);