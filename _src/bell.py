# Live bell timer for the home page (4 languages). Uses BELLS from build.py and the class chosen on the timetable page.
import json

T = {
 "title": ("Qońıraw taymeri", "Bell timer", "Qo‘ng‘iroq taymeri", "Таймер звонков"),
 "live": ("Jonlı", "Live", "Jonli", "Онлайн"),
 "lesson": ("{p}-sabaq", "Lesson {p}", "{p}-dars", "{p}-й урок"),
 "brk": ("Tánepis", "Break", "Tanaffus", "Перемена"),
 "lunch": ("Túslik tánepis", "Lunch break", "Tushlik tanaffusi", "Обеденный перерыв"),
 "until": ("{t} qońırawına shekem", "until the bell at {t}", "{t} dagi qo‘ng‘iroqqacha", "до звонка в {t}"),
 "before": ("Sabaqlar baslanıwına", "Until lessons start", "Darslar boshlanishiga", "До начала уроков"),
 "starts": ("Birinshi qońıraw {t} de", "First bell at {t}", "Birinchi qo‘ng‘iroq {t} da", "Первый звонок в {t}"),
 "done": ("Búgingi sabaqlar tamamlandı", "School day is over", "Bugungi darslar tugadi", "Уроки на сегодня закончились"),
 "weekend": ("Dem alıs kúni", "Weekend", "Dam olish kuni", "Выходной"),
 "next": ("Keyingi sabaq: {d}, {t}", "Next lesson: {d} at {t}", "Keyingi dars: {d}, {t}", "Следующий урок: {d}, {t}"),
 "tom": ("erteń", "tomorrow", "ertaga", "завтра"),
 "nextl": ("Keyingi: {l} · {t}", "Next: {l} · {t}", "Keyingi: {l} · {t}", "Далее: {l} · {t}"),
 "lastl": ("Bul — sońǵı sabaq", "This is the last lesson", "Bu — oxirgi dars", "Это последний урок"),
 "prog": ("Kún: {a} / {n} sabaq", "Day: {a} of {n} lessons", "Kun: {a} / {n} dars", "День: {a} из {n} уроков"),
 "choose": ("Klasıńızdı tańlań — pándi kórsetemiz", "Choose your class to see the subject", "Sinfingizni tanlang — fanni ko‘rsatamiz", "Выберите класс — покажем предмет"),
 "cls": ("klass", "class", "sinf", "класс"),
 "dunit": ("kún", "d", "kun", "д"),
 "tt": ("Sabaq kestesi", "Timetable", "Dars jadvali", "Расписание"),
 "days": (("Dúyshembi", "Siyshembi", "Sárshembi", "Piyshembi", "Juma", "Shembi", "Ekshembi"),
          ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"),
          ("Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"),
          ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")),
}

def html(i, bells, subj, tt_href):
    data = {"b": bells, "s": subj, "t": {k: v[i] for k, v in T.items()}}
    pills = ""
    for k, (a, e) in enumerate(bells, 1):
        pills += f'<li data-p="{k}"><b>{k}</b><span>{a}</span></li>'
        if k < len(bells):
            gap = (int(bells[k][0].split(":")[0]) * 60 + int(bells[k][0].split(":")[1])) - (int(e.split(":")[0]) * 60 + int(e.split(":")[1]))
            pills += f'<li class="bgap{" lunch" if gap >= 20 else ""}" data-g="{k}" aria-hidden="true"></li>'
    C = 2 * 3.14159 * 54
    return f"""<section class="bellsec" aria-labelledby="bellh"><div class="wrap"><div class="bell" id="bell" data-c="{C:.1f}">
<div class="bltop"><span class="blive"><i></i>{T['live'][i]}</span><h2 id="bellh">{T['title'][i]}</h2><span class="bclock" id="bclock">--:--</span></div>
<div class="blmain"><div class="bring"><svg viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="54" class="b0"/><circle cx="60" cy="60" r="54" class="b1" id="barc" stroke-dasharray="0 {C:.1f}" transform="rotate(-90 60 60)"/></svg>
<div><span class="bstate" id="bstate">…</span><b class="bcount" id="bcount">--:--</b><span class="buntil" id="buntil"></span></div></div>
<div class="bside"><p class="bsubj" id="bsubj"></p><p class="bnext" id="bnext"></p><div class="bprog"><span id="bprogt"></span><div><i id="bprogb"></i></div></div>
<a class="bchoose" id="bchoose" href="{tt_href}">{T['choose'][i]} →</a></div></div>
<ol class="bline" id="bline">{pills}</ol>
</div></div></section>
<script id="belldata" type="application/json">{json.dumps(data, ensure_ascii=False, separators=(",", ":"))}</script>"""

JS = r"""
  const bd=document.getElementById('belldata');
  if(bd){const D=JSON.parse(bd.textContent),T=D.t,B=D.b,$=id=>document.getElementById(id),C=+$('bell').dataset.c;
    const mm=s=>{const[h,m]=s.split(':');return(+h*60+ +m)*60},pad=n=>String(n).padStart(2,'0');
    const fmt=s=>{s=Math.max(0,Math.round(s));if(s>=86400){const d=Math.floor(s/86400),r=s%86400;return`${d} ${T.dunit} ${Math.floor(r/3600)}:${pad(Math.floor(r%3600/60))}`}const h=Math.floor(s/3600),m=Math.floor(s%3600/60),x=s%60;return h?`${h}:${pad(m)}:${pad(x)}`:`${pad(m)}:${pad(x)}`};
    const esc=s=>String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
    let cls=null,ALL=null;const rc=()=>{try{return(localStorage.getItem('ttmode')||'class')==='class'?localStorage.getItem('ttcls'):null}catch(e){return null}};
    fetch(document.querySelector('link[rel=icon][href$="logo.png"]').href.replace(/logo\.png$/,'timetable.json')).then(r=>r.json()).then(j=>{ALL=j.classes;tick()}).catch(()=>{});
    const K=['mon','tue','wed','thu','fri'];
    const subj=(wd,p)=>{const TT=ALL&&cls?ALL[cls]:null;if(!TT||wd>4)return null;const d=TT[K[wd]]||{},x=d[p];if(!x)return null;const k=x[0][0];return(D.s[k]||[k])[0]};
    const lis=[...document.querySelectorAll('#bline li')];
    function now(){const p={};new Intl.DateTimeFormat('en-US',{timeZone:'Asia/Samarkand',weekday:'short',hour:'2-digit',minute:'2-digit',second:'2-digit',hourCycle:'h23'}).formatToParts(new Date()).forEach(x=>p[x.type]=x.value);
      return{wd:['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(p.weekday),s:+p.hour*3600+ +p.minute*60+ +p.second,h:p.hour,m:p.minute}}
    function nextDay(wd){let d=1;while((wd+d)%7>4)d++;return d}
    function tick(){cls=rc();$('bchoose').hidden=!!cls;const N=now(),wd=N.wd,s=N.s,first=mm(B[0][0]),last=mm(B[B.length-1][1]);
      $('bclock').textContent=`${T.days[wd]}, ${N.h}:${N.m}`;
      let state='',left=0,total=1,until='',next='',cur=0,gap=0,done=0,mode='';
      if(wd>4||s>=last){const d=wd>4?nextDay(wd):nextDay(wd);left=d*86400-s+first;total=left;mode='off';
        state=wd>4?T.weekend:T.done;until=T.before;next=T.next.replace('{d}',d===1&&wd<=4?T.tom:T.days[(wd+d)%7]).replace('{t}',B[0][0]);done=wd>4?0:B.length}
      else if(s<first){left=first-s;total=Math.max(left,3600);state=T.before;until=T.starts.replace('{t}',B[0][0]);mode='pre'}
      else{for(let k=0;k<B.length;k++){const a=mm(B[k][0]),e=mm(B[k][1]);
          if(s>=a&&s<e){cur=k+1;left=e-s;total=e-a;state=T.lesson.replace('{p}',cur);until=T.until.replace('{t}',B[k][1]);done=k;mode='les';
            next=k+1<B.length?T.nextl.replace('{l}',T.lesson.replace('{p}',k+2)).replace('{t}',B[k+1][0]):T.lastl;break}
          if(k+1<B.length&&s>=e&&s<mm(B[k+1][0])){gap=k+1;const n=mm(B[k+1][0]);left=n-s;total=n-e;state=(total>=1200?T.lunch:T.brk);until=T.until.replace('{t}',B[k+1][0]);done=k+1;mode='brk';
            next=T.nextl.replace('{l}',T.lesson.replace('{p}',k+2)).replace('{t}',B[k+1][0]);break}}}
      const bell=$('bell');bell.dataset.m=mode;
      $('bstate').textContent=state;$('bcount').textContent=fmt(left);$('buntil').textContent=until;$('bnext').textContent=next;
      const f=mode==='off'?0:Math.min(1,Math.max(0,1-left/total));$('barc').setAttribute('stroke-dasharray',`${(C*f).toFixed(1)} ${C}`);$('barc').style.opacity=f>0?1:0;
      $('bprogt').textContent=T.prog.replace('{a}',done).replace('{n}',B.length);$('bprogb').style.width=(done/B.length*100)+'%';
      const sp=mode==='les'?cur:mode==='brk'?gap+1:mode==='pre'?1:0,sj=sp?subj(wd,sp):null;
      $('bsubj').innerHTML=cls?(`<b>${esc(cls)} ${esc(T.cls)}</b>`+(sj&&mode==='les'?` · ${esc(sj)}`:'')):'';if(sj&&mode!=='les')$('bnext').textContent=(mode==='pre'?T.nextl.replace('{l}',T.lesson.replace('{p}',1)).replace('{t}',B[0][0]):next)+' · '+sj;$('bsubj').hidden=!cls;
      const wk=wd<=4;lis.forEach(li=>{const p=+li.dataset.p||0,g=+li.dataset.g||0,end=p?mm(B[p-1][1]):mm(B[g][0]);
        li.classList.toggle('past',wk&&s>=end);li.classList.toggle('now',(mode==='les'&&p===cur)||(mode==='brk'&&g===gap))})}
    tick();setInterval(tick,1000)}"""
