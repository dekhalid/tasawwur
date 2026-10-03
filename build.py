#!/usr/bin/env python3
"""build.py — the Tasawwur marketing page: / (Arabic) and /en/ (English), one template."""
import os, html
D = os.path.dirname(os.path.abspath(__file__))
STORE = 'https://apps.apple.com/app/id6784710045'
PRIVACY = 'https://dekhalid.github.io/dhakrle-legal/privacy.html'
SUPPORT = 'https://dhakrle-proxy.dhakrle.workers.dev/support'
EULA = 'https://www.apple.com/legal/internet-services/itunes/dev/stdeula/'
BASE = 'https://dekhalid.github.io/tasawwur/'
T = {
 'ar': dict(dir='rtl', lang='ar', name='تصوّر', title='تصوّر — يشرح لك دروسك بالرسم',
   desc='تصوّر يشرح لك دروسك بالرسم، ويحوّل محاضراتك إلى دليل مذاكرة مرسوم، ومعه مدرّس صوتي يرسم ويسألك.',
   h1='يشرح لك دروسك<br>بالرسم',
   lead='اسأل عن أي فكرة في مادتك وتصلك إجابة قصيرة مع رسم يوضّحها، ولخّص محاضرتك بدليل مذاكرة مرسوم، وذاكر بصوتك مع مدرّس يرسم ويسألك.',
   meta='للآيفون والآيباد · بالعربية والإنجليزية · بدون حساب',
   feats=[('يرسم لك الفكرة','اسأل عن أي فكرة وتصلك إجابة مختصرة مع رسم، وأسماء الأجزاء مكتوبة عليه.'),
          ('لخّص محاضرتك بالرسم','ملخّص سريع أو دليل مذاكرة كامل من ملفك، فيه رسوم للأفكار المهمة، ومراجَع على محاضرتك.'),
          ('مدرّس صوتي','ذاكر بصوتك باللهجة السعودية؛ يرسم الفكرة ويؤشّر على كل جزء وهو يشرحه، ويختم بسؤال سريع.'),
          ('ملفاتك مرتّبة','مجلد لكل مادة بضغطة، و«كمّل من ص …» يرجّعك للصفحة اللي وقفت عندها.'),
          ('اكتب على محاضرتك','بالقلم على الآيباد أو بإصبعك على الآيفون، بألوان للقلم والتظليل ونص وصور على الصفحة.'),
          ('اختبرني وصحّح خطواتي','أسئلة من ملفك تركّز على اللي أخطأت فيه، وصحّح حلّك وشوف وين الغلط.')],
   who='للجامعة والثانوي والمتوسط، وتقدر تسأله عن مسائل القدرات والتحصيلي.',
   plans='ابدأ مجانًا: ٥ طلبات و١٠ دقائق صوت يوميًا. تصوّر بلس يعطيك أكثر، باشتراك أسبوعي أو شهري أو كل ٣ أشهر.',
   feat_h='وش يقدر يسوي', who_h='لمين', plans_h='الاشتراك', badge='img/badge-ar.svg', badge_alt='حمّله من App Store',
   foot=[('سياسة الخصوصية',PRIVACY),('الدعم',SUPPORT),('شروط الاستخدام',EULA),('English','en/')],
   copy='© ٢٠٢٦ تصوّر', shot='img/ar-{}.jpg', root='', shots_alt=['يرسم لك الفكرة','لخّص محاضرتك بالرسم','ذاكر بصوتك','كل ملفاتك مرتّبة','اكتب على محاضرتك'],
   font="'IBM Plex Sans Arabic'"),
 'en': dict(dir='ltr', lang='en', name='Tasawwur', title='Tasawwur — your courses, explained with drawings',
   desc='Tasawwur explains your courses with drawings, turns your lectures into illustrated study guides, and gives you a voice tutor that draws and quizzes you.',
   h1='Your courses,<br>explained with drawings',
   lead='Ask about any idea and get a short answer with a drawing that shows it, summarize your lecture into an illustrated study guide, and study out loud with a tutor that draws and asks you.',
   meta='For iPhone and iPad · Arabic and English · No account needed',
   feats=[('Draws the idea','Ask about any idea and get a short answer with a drawing, its parts labeled.'),
          ('Summarize with drawings','A quick summary or a full study guide from your file, with drawings of the key ideas, checked against your lecture.'),
          ('A voice tutor','Study out loud in Arabic or English; the tutor draws the idea, points at each part as it explains, and ends with a quick check.'),
          ('Your files, sorted','One tap makes a folder per course, and "Continue from p. ..." takes you back to the page you stopped on.'),
          ('Write on your lectures','With the Apple Pencil on iPad or your finger on iPhone, with pen and highlighter colors, text and photos on the page.'),
          ('Quiz me, check my steps','Questions from your file that focus on what you missed, and step checks that show where a solution went wrong.')],
   who='For university, high school and middle school, including Qudurat and Tahsili questions.',
   plans='Start free: 5 requests and 10 voice minutes a day. Tasawwur Plus gives you more, billed weekly, monthly or every 3 months.',
   feat_h='What it does', who_h='Who it is for', plans_h='Plans', badge='../img/badge-en.svg', badge_alt='Download on the App Store',
   foot=[('Privacy Policy',PRIVACY),('Support',SUPPORT),('Terms of Use',EULA),('العربية','../')],
   copy='© 2026 Tasawwur', shot='../img/en-{}.jpg', root='../', shots_alt=['Draws the idea','Summarize with drawings','Study out loud','All your files, sorted','Write on your lectures'],
   font="'IBM Plex Sans Arabic'"),
}
def page(c, url):
    shots = ''.join(f'<figure><img src="{c["shot"].format(i)}" alt="{html.escape(a)}" loading="lazy" width="600" height="1300"></figure>'
                    for i, a in enumerate(c['shots_alt'], 1))
    feats = ''.join(f'<li><h3>{html.escape(h)}</h3><p>{html.escape(p)}</p></li>' for h, p in c['feats'])
    foot = ' · '.join(f'<a href="{u}">{html.escape(t)}</a>' for t, u in c['foot'])
    r = c['root']
    return f'''<!doctype html>
<html lang="{c['lang']}" dir="{c['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(c['title'])}</title>
<meta name="description" content="{html.escape(c['desc'])}">
<meta name="apple-itunes-app" content="app-id=6784710045">
<meta property="og:type" content="website"><meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(c['title'])}"><meta property="og:description" content="{html.escape(c['desc'])}">
<meta property="og:image" content="{BASE}img/og.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}img/favicon-64.png"><link rel="apple-touch-icon" href="{r}img/apple-touch-icon.png">
<link rel="alternate" hreflang="ar" href="{BASE}"><link rel="alternate" hreflang="en" href="{BASE}en/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root {{ --bg:#0b0d18; --bg2:#121628; --cream:#f6e7c9; --amber:#e2ae58; --text:#e6e3ee; --muted:#a9a6b8; --line:rgba(226,174,88,.25); }}
* {{ box-sizing:border-box; }}
html,body {{ margin:0; background:var(--bg); color:var(--text); font-family:{c['font']}, -apple-system, system-ui, sans-serif; }}
body {{ background: radial-gradient(1200px 700px at 50% -10%, #221c3d 0%, rgba(11,13,24,0) 60%),
        radial-gradient(1px 1px at 12% 18%, #fff7 50%, transparent 51%), radial-gradient(1px 1px at 78% 12%, #fff6 50%, transparent 51%),
        radial-gradient(1.5px 1.5px at 62% 30%, #fff5 50%, transparent 51%), radial-gradient(1px 1px at 30% 42%, #fff5 50%, transparent 51%),
        radial-gradient(1.5px 1.5px at 88% 46%, #fff4 50%, transparent 51%), var(--bg); background-attachment: scroll; line-height:1.7; }}
a {{ color:var(--cream); }}
.wrap {{ max-width:1080px; margin:0 auto; padding:0 20px; }}
header.top {{ display:flex; align-items:center; justify-content:space-between; padding:18px 0; }}
.brand {{ display:flex; align-items:center; gap:12px; font-weight:700; font-size:20px; color:var(--cream); text-decoration:none; }}
.brand img {{ width:40px; height:40px; border-radius:10px; }}
.lang {{ color:var(--muted); text-decoration:none; font-size:15px; }}
.hero {{ text-align:center; padding:48px 0 28px; }}
.hero img.icon {{ width:96px; height:96px; border-radius:22px; box-shadow:0 10px 40px rgba(226,174,88,.25); }}
.hero h1 {{ font-size:clamp(34px,6vw,58px); line-height:1.2; margin:22px 0 14px; color:var(--cream); font-weight:700; }}
.hero p.lead {{ max-width:720px; margin:0 auto; font-size:clamp(16px,2.2vw,19px); color:var(--text); }}
.hero .meta {{ margin-top:12px; color:var(--muted); font-size:14px; }}
.badge {{ display:inline-block; margin-top:26px; }}
.badge img {{ height:56px; width:auto; display:block; }}
.gallery {{ display:flex; direction:ltr; gap:16px; overflow-x:auto; scroll-snap-type:x mandatory; padding:28px 20px 12px; margin:0 -20px; }}
.gallery figure {{ flex:0 0 min(62vw,220px); margin:0; scroll-snap-align:center; }}
.gallery img {{ width:100%; height:auto; border-radius:22px; display:block; border:1px solid var(--line); }}
@media (min-width: 900px) {{ .gallery {{ justify-content:center; overflow:visible; }} .gallery figure {{ flex-basis:196px; }} }}
section {{ padding:36px 0; }}
h2 {{ color:var(--cream); font-size:26px; margin:0 0 18px; }}
ul.feats {{ list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:14px; }}
ul.feats li {{ background:var(--bg2); border:1px solid var(--line); border-radius:18px; padding:18px 20px; }}
ul.feats h3 {{ margin:0 0 6px; font-size:18px; color:var(--amber); }}
ul.feats p {{ margin:0; color:var(--text); font-size:15.5px; }}
.card {{ background:var(--bg2); border:1px solid var(--line); border-radius:18px; padding:18px 20px; font-size:16px; }}
.cta {{ text-align:center; padding:40px 0 20px; }}
footer {{ border-top:1px solid rgba(255,255,255,.08); margin-top:30px; padding:24px 0 40px; color:var(--muted); font-size:14px; text-align:center; }}
footer a {{ color:var(--muted); }}
</style>
</head>
<body>
<div class="wrap">
<header class="top"><a class="brand" href="{r or './'}"><img src="{r}img/icon-256.png" alt="">{html.escape(c['name'])}</a>
<a class="lang" href="{c['foot'][-1][1]}">{html.escape(c['foot'][-1][0])}</a></header>
<main>
<div class="hero">
<img class="icon" src="{r}img/icon-256.png" alt="{html.escape(c['name'])}">
<h1>{c['h1']}</h1>
<p class="lead">{html.escape(c['lead'])}</p>
<div class="meta">{html.escape(c['meta'])}</div>
<a class="badge" href="{STORE}"><img src="{c['badge']}" alt="{html.escape(c['badge_alt'])}"></a>
</div>
<div class="gallery">{shots}</div>
<section><h2>{html.escape(c['feat_h'])}</h2><ul class="feats">{feats}</ul></section>
<section><h2>{html.escape(c['who_h'])}</h2><div class="card">{html.escape(c['who'])}</div></section>
<section><h2>{html.escape(c['plans_h'])}</h2><div class="card">{html.escape(c['plans'])}</div></section>
<div class="cta"><a class="badge" href="{STORE}"><img src="{c['badge']}" alt="{html.escape(c['badge_alt'])}"></a></div>
</main>
<footer>{foot}<br>{html.escape(c['copy'])}</footer>
</div>
</body>
</html>
'''
open(os.path.join(D, 'index.html'), 'w').write(page(T['ar'], BASE))
os.makedirs(os.path.join(D, 'en'), exist_ok=True)
open(os.path.join(D, 'en', 'index.html'), 'w').write(page(T['en'], BASE + 'en/'))
open(os.path.join(D, '.nojekyll'), 'w').write('')
print('built')
