from aiogram import types
from dispatcher import dp, bot


@dp.message_handler(commands=["privacy"])
async def cmd_privacy(message: types.Message):
    bot_info = await bot.get_me()
    bot_username = bot_info.username
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"<b>Политика конфиденциальности @{bot_username}.</b>\n\n<b>Дата вступления в силу: 4 июля 2024 г.</b>\n\n<b>Добро пожаловать в @{bot_username}!</b> Мы уделяем приоритетное внимание вашей конфиденциальности и стремимся обеспечить защиту ваших личных данных. В данной Политике конфиденциальности описывается, как мы собираем, используем и защищаем вашу информацию в соответствии с рекомендациями <b>Telegram</b>, требованиями <b>Apple App Store</b> и <b>Google Play Store</b>.\n\n<b>1. Информация, которую мы собираем:</b>\nДля обеспечения корректной работы нашего бота мы можем собирать следующую информацию из вашего профиля Telegram:\n• <b>Идентификаторы файлов (только то что вы отправили боту, фото, видео, GIF-анимация, документ).</b>\n\n<b>2. Как мы используем вашу информацию:</b>\nИнформация, которую мы собираем, используется исключительно с целью предоставления и улучшения наших услуг. В частности, мы используем вашу информацию для:\n<b>• Сохранения и предоставления ссылок на загруженные вами файлы.</b>\n\n<b>3. Хранение и безопасность данных:</b>\nИдентификаторы файлов и связанная с ними информация сохраняются в нашей базе данных только для того, чтобы предоставить вам доступ к файлам и их обмен. Мы реализуем соответствующие технические и организационные меры для защиты ваших данных от несанкционированного доступа, изменения или уничтожения.\n\n<b>4. Обмен и продажа данных:</b>\nМы не продаем, не обмениваем и не передаем иным образом вашу личную информацию сторонним лицам. Ваши данные используются исключительно в контексте предоставления вам услуг нашего бота и не передаются никаким сторонним службам.\n\n<b>5. Соблюдение требований законодательства:</b>\nМы соблюдаем все соответствующие законодательные требования и отраслевые стандарты, в том числе установленные <b>Telegram</b>, <b>Apple App Store</b> и <b>Google Play Store</b>. В случае юридического обязательства мы можем раскрыть вашу информацию, если этого требует закон, постановление или судебный процесс.\n\n<b>6. Изменения в Политике конфиденциальности:</b>\nМы можем время от времени обновлять Политику конфиденциальности, чтобы отражать изменения в нашей практике или юридических требованиях. Любые обновления будут публиковаться на этой странице с указанием даты вступления в силу. Мы рекомендуем вам периодически просматривать Политику конфиденциальности.\n\n<b>7. Свяжитесь с нами:</b>\nЕсли у вас есть какие-либо вопросы или сомнения по поводу Политики конфиденциальности или наших методов обработки данных, свяжитесь с нами по адресу <b>@OFFpolice</b>.\n\n<b>Используя @{bot_username}, вы соглашаетесь с условиями, изложенными в Политике конфиденциальности.</b>",
        parse_mode="HTML"
    )