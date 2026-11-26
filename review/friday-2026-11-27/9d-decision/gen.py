import subprocess,glob,os
CH=glob.glob(os.path.expanduser("~/.cache/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell"))[0]
RED,BLK,PAPER="#d7261e","#0d0d0d","#f5f2ec"
css=f"""<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@600;700&family=Inter:wght@400;500;600;700&display=block" rel="stylesheet"><style>
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1350px;overflow:hidden;background:{BLK};font-family:Inter,'Noto Sans CJK HK',sans-serif;color:{PAPER}}}
.ph{{position:absolute;inset:0;background-size:cover;background-position:var(--pos,center)}}
.sh{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,13,13,.55) 0%,rgba(13,13,13,0) 26%,rgba(13,13,13,0) 42%,rgba(13,13,13,.88) 72%,{BLK} 100%)}}
.wrap{{position:absolute;inset:0;padding:60px;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:center}}.lock{{display:flex;align-items:center;gap:16px;font-family:Unbounded;font-weight:600;font-size:24px}}.lock img{{height:70px}}.lock .x{{opacity:.6;font-size:20px}}.lock .b{{height:44px}}
.pill{{font-weight:700;font-size:18px;letter-spacing:.12em;text-transform:uppercase;border:2px solid rgba(245,242,236,.6);border-radius:999px;padding:10px 20px;background:rgba(13,13,13,.35)}}
.body{{margin-top:auto}}.tag{{display:inline-block;background:{RED};color:#fff;font-weight:700;font-size:20px;letter-spacing:.14em;text-transform:uppercase;padding:9px 18px;border-radius:6px}}
h1{{font-family:Unbounded;font-weight:700;font-size:96px;line-height:1.0;letter-spacing:-.02em;margin-top:22px}}h1 .r{{color:{RED}}}
.zh{{font-family:'Noto Sans CJK HK';font-weight:700;font-size:44px;margin-top:18px;color:#e6e0d6}}
.sub{{font-size:29px;line-height:1.38;font-weight:500;color:#ddd6cb;margin-top:20px;max-width:900px}}
.legs{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:22px}}.leg{{background:rgba(245,242,236,.1);border-left:5px solid {RED};padding:14px 18px;font-size:22px;font-weight:600}}.leg b{{display:block;font-family:Unbounded;font-size:18px;color:{RED};margin-bottom:4px;letter-spacing:.06em}}
.foot{{display:flex;justify-content:space-between;align-items:center;margin-top:34px;padding-top:24px;border-top:1.5px solid rgba(245,242,236,.25)}}.url{{background:{RED};color:#fff;font-weight:700;font-size:26px;border-radius:999px;padding:16px 30px}}.sl{{font-family:Unbounded;font-size:18px;letter-spacing:.14em;text-transform:uppercase;color:rgba(245,242,236,.75)}}
.cr{{position:absolute;right:60px;top:150px;font-size:13px;color:rgba(245,242,236,.55);letter-spacing:.06em}}
</style>"""
top=lambda p:f'<div class="top"><div class="lock"><img src="medallion_clean_white.png"><span class="x">×</span><img class="b" src="bibly_icon_96.png">Bibly</div><div class="pill">{p}</div></div>'
def foot(u="bibly.run/events"): return f'<div class="foot"><div class="url">{u}</div><div class="sl">Pain Is Inevitable.</div></div>'
def slide(img,pos,pill,inner,u="bibly.run/events"):
    return f'<div class="ph" style="background-image:url({img});--pos:{pos}"></div><div class="sh"></div><div class="wrap">{top(pill)}<div class="body">{inner}</div>{foot(u)}</div>'
S={}
S['ig-1']=slide('dragons_misty_rock.jpg','55% 30%','The 9 Dragons 2027','<span class="tag">25 km sold out</span><h1>Decision<br><span class="r">time.</span></h1><div class="zh">係時候決定</div><div class="sub">The 25 km is full. Two ways to still be on the start line in February.</div>')
S['ig-2']=slide('dragons_woman_steps.jpg','50% 35%','Option 1','<span class="tag">Selling fast</span><h1>Step up<br>to the <span class="r">50 km.</span></h1><div class="zh">升級挑戰 50 公里</div><div class="sub">The classic. Sun 28 Feb, 07:30 start at Tai Po Tau. Six aid stations, 21:30 cut-off, same finish line as the 9th Dragon.</div>')
S['ig-3']=slide('dragons_statue_ridge.jpg','45% 40%','Option 2','<span class="tag">Team of four</span><h1 style="font-size:84px">Find three<br><span class="r">friends.</span></h1><div class="zh">搵三個朋友　組隊接力</div><div class="sub">50 Mile Relay. Midnight start, Sat 27 Feb. One wristband passed hand to hand to the finish.</div><div class="legs"><div class="leg"><b>LEG 1</b>Start to CP2 Wun Yiu Road</div><div class="leg"><b>LEG 2</b>CP2 to CP4 Fanling</div><div class="leg"><b>LEG 3</b>CP4 to CP6 Bride\'s Pool</div><div class="leg"><b>LEG 4</b>CP6 to Tai Po Tau</div></div>')
S['ig-4']=slide('finish_champion.jpg','50% 25%','Your call','<span class="tag">Register on Bibly</span><h1>50 km or<br><span class="r">relay.</span></h1><div class="zh">50 公里定接力　你揀</div><div class="sub">Choose your race at bibly.run/events. Link in bio.</div>','bibly.run/events')
S['fb-bibly']=slide('dragons_radar_ridge.jpg','60% 35%','The 9 Dragons 2027','<span class="tag">25 km sold out</span><h1 style="font-size:84px">50 km or<br><span class="r">relay?</span></h1><div class="zh">50 公里定接力</div><div class="sub">Step up to the 50 km, selling fast. Or bring three friends to the 50 Mile Relay.</div>')
S['fb-9d']=slide('dragons_village_road.jpg','45% 40%','The 9 Dragons 2027','<span class="tag">Decision time</span><h1 style="font-size:84px">Step up.<br><span class="r">Or team up.</span></h1><div class="zh">升級　或者組隊</div><div class="sub">25 km is sold out. The 50 km is selling fast. The 50 Mile Relay takes a team of four.</div>')
for k,s in S.items():
    h=f"{os.getcwd()}/{k}.html";open(h,"w").write("<html><head><meta charset='utf-8'>"+css+"</head><body>"+s+"</body></html>")
    subprocess.run([CH,"--headless","--no-sandbox","--disable-gpu","--hide-scrollbars","--window-size=1080,1350","--virtual-time-budget=6000",f"--screenshot={os.getcwd()}/9d-decision-{k}.png","file://"+h],capture_output=True)
from PIL import Image
ims=[Image.open(f'9d-decision-{k}.png').convert('RGB') for k in S]
W=540;sh=Image.new('RGB',(W*3+40,675*2+30),'white')
for i,im in enumerate(ims): sh.paste(im.resize((W,675)),(10+(i%3)*(W+10),10+(i//3)*685))
sh.save('9d-decision-preview.jpg',quality=86)
