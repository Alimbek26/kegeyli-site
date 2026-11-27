# Telegram channel feed: embeds the latest public posts with Telegram's official post widget.
# To update: put the newest post numbers first (open t.me/s/Kegeyliqanigelestirilgenmektebi to see them).
CHANNEL = "Kegeyliqanigelestirilgenmektebi"
POSTS = [8839, 8837, 8836, 8831, 8830, 8826]
T = {
 "h": ("Telegram kanalımızdan", "From our Telegram channel", "Telegram kanalimizdan", "Из нашего Telegram-канала"),
 "p": ("Mektep turmısınıń eń sońǵı jańalıqları — tikkeley kanalımızdan.", "The latest school news, straight from our channel.",
       "Maktab hayotining eng so‘nggi yangiliklari — to‘g‘ridan-to‘g‘ri kanalimizdan.", "Свежие новости школы — прямо из нашего канала."),
 "join": ("Kanalǵa aǵza bolıw", "Join the channel", "Kanalga obuna bo‘lish", "Подписаться на канал"),
 "more": ("Jáne kórsetiw", "Show more", "Yana ko‘rsatish", "Показать ещё"),
}
TG_ICON = '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M21.900 4.300l-3.200 15.100c-.2 1-.9 1.300-1.800.8l-4.900-3.600-2.400 2.300c-.3.300-.5.500-1 .5l.4-5 9.100-8.200c.4-.4-.1-.6-.6-.2L6.300 13.100l-4.800-1.500c-1-.3-1.100-1 .2-1.500L20.500 2.900c.9-.3 1.600.2 1.400 1.400z"/></svg>'
def html(i, n, show_more=True):
    lang = ["kaa", "en", "uz", "ru"][i]
    items = ""
    for k, p in enumerate(POSTS[:n]):
        items += (f'<div class="tgi"{" hidden" if k >= 3 and show_more else ""}><script async src="https://telegram.org/js/telegram-widget.js?22" '
                  f'data-telegram-post="{CHANNEL}/{p}" data-width="100%" data-userpic="false" data-dark-auto="1"></script></div>')
    more = (f'<button type="button" class="btn s tgmore" onclick="this.previousElementSibling.querySelectorAll(\'.tgi[hidden]\').forEach(function(x){{x.hidden=false}});this.remove()">{T["more"][i]}</button>'
            if show_more and n > 3 else "")
    return (f'<div class="tgfeed"><div class="tghead"><span class="tglogo">{TG_ICON}</span><div><h3>{T["h"][i]}</h3><p>{T["p"][i]}</p></div>'
            f'<a class="btn p tgjoin" href="https://t.me/{CHANNEL}" rel="noopener">{T["join"][i]}</a></div><div class="tggrid">{items}</div>{more}</div>')
