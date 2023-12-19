import sqlite3

db = sqlite3.connect('table.db')

c = db.cursor()

c.execute("""CREATE TABLE monday(
    number text,
    title text
)""")
c.execute("INSERT INTO monday VALUES ('🧠1-я пара (8:00-9:30)🧠', '<----->')")
c.execute("INSERT INTO monday VALUES ('🧠2-я пара (9:45-11:20)🧠', '<----->')")
c.execute("INSERT INTO monday VALUES ('🧠3-я пара (11:30-13:05)🧠', 'Лек. Тех. предпр. (чет/неч)[303] / Лек. Проф. этика (чет/неч)[312]')")
c.execute("INSERT INTO monday VALUES ('🧠4-я пара (13:30-15:05)🧠', 'Пр. Проф.Этика (чет/неч)[312] / Пр. Тех. предпр. (чет/неч)[303]')")
c.execute("INSERT INTO monday VALUES ('🧠5-я пара (15:15-16:50)🧠', 'ЛР Python (чет/неч)[213] / Разработка ПО (5,9,13,17|4,8,12,16) [208]')")
c.execute("INSERT INTO monday VALUES ('🧠6-я пара (17:00-18:35)🧠', 'ЛР Python (чет/неч)[213] / Разработка ПО (5,9,13,17|4,8,12,16) [208]')")

c.execute("""CREATE TABLE tuesday(
    number text,
    title text
)""")
c.execute("INSERT INTO tuesday VALUES ('🧠1-я пара (8:00-9:30)🧠', '<----->')")
c.execute("INSERT INTO tuesday VALUES ('🧠2-я пара (9:45-11:20)🧠', 'Пр. Проектная деятельность [213]')")
c.execute("INSERT INTO tuesday VALUES ('🧠3-я пара (11:30-13:05)🧠', 'ЛР МОАС (чет/неч)[215] / ЛР РПИ (чет/неч) [210]')")
c.execute("INSERT INTO tuesday VALUES ('🧠4-я пара (13:30-15:05)🧠', 'ЛР МОАС (чет/неч)[215] / ЛР РПИ (чет/неч) [210]')")
c.execute("INSERT INTO tuesday VALUES ('🧠5-я пара (15:15-16:50)🧠', 'ФИЗ-РА СТРОЯК')")
c.execute("INSERT INTO tuesday VALUES ('🧠6-я пара (17:00-18:35)🧠', '<----->')")

c.execute("""CREATE TABLE wednesday(
    number text,
    title text
)""")
c.execute("INSERT INTO wednesday VALUES ('🧠ВЕСЬ ДЕНЬ🧠', 'ВОЕННАЯ ПОДГОТОВКА')")

c.execute("""CREATE TABLE thursday(
    number text,
    title text
)""")
c.execute("INSERT INTO thursday VALUES ('🧠1-я пара (8:00-9:30)🧠', 'ЛР МОАС (чет/неч)[215]')")
c.execute("INSERT INTO thursday VALUES ('🧠2-я пара (9:45-11:20)🧠', 'ЛР МОАС (чет/неч)[215]')")
c.execute("INSERT INTO thursday VALUES ('🧠3-я пара (11:30-13:05)🧠', 'Лек. МОАС [111]')")
c.execute("INSERT INTO thursday VALUES ('🧠4-я пара (13:30-15:05)🧠', 'Лек. РПИ [210]')")
c.execute("INSERT INTO thursday VALUES ('🧠5-я пара (15:15-16:50)🧠', 'ЛР РПИ (2,6,10,14|4,8,12,16)[210]')")
c.execute("INSERT INTO thursday VALUES ('🧠6-я пара (17:00-18:35)🧠', 'ЛР РПИ (2,6,10,14|4,8,12,16)[210]')")

c.execute("""CREATE TABLE friday(
    number text,
    title text
)""")
c.execute("INSERT INTO friday VALUES ('🧠1-я пара (8:00-9:30)🧠', '<----->')")
c.execute("INSERT INTO friday VALUES ('🧠2-я пара (9:45-11:20)🧠', 'ЛР Python (4,8,12,16|6,10,14,18)[213]')")
c.execute("INSERT INTO friday VALUES ('🧠3-я пара (11:30-13:05)🧠', 'ЛР Python (4,8,12,16|6,10,14,18)[213] / Пр. Проф. этика (чет/неч)[111]')")
c.execute("INSERT INTO friday VALUES ('🧠4-я пара (13:30-15:05)🧠', 'Лек. Python [213]')")
c.execute("INSERT INTO friday VALUES ('🧠5-я пара (15:15-16:50)🧠', 'ЛР Разработка ПО (чет/неч)[215]')")
c.execute("INSERT INTO friday VALUES ('🧠6-я пара (17:00-18:35)🧠', 'ЛР Разработка ПО (чет/неч)[215]')")

c.execute("""CREATE TABLE saturday(
    number text,
    title text
)""")
c.execute("INSERT INTO saturday VALUES ('🧠1-я пара (8:00-9:30)🧠', '<----->')")
c.execute("INSERT INTO saturday VALUES ('🧠2-я пара (9:45-11:20)🧠', '<----->/ЛР Инт. собственность (2,6,10,14|4,8,12,16)[210]')")
c.execute("INSERT INTO saturday VALUES ('🧠3-я пара (11:30-13:05)🧠', 'Лек. Инт. собственность [307]/ЛР Инт. собственность (2,6,10,14|4,8,12,16)[210]')")
c.execute("INSERT INTO saturday VALUES ('🧠4-я пара (13:30-15:05)🧠', 'Лек. Разработка ПО [307]')")
c.execute("INSERT INTO saturday VALUES ('🧠5-я пара (15:15-16:50)🧠', 'ФИЗ-РА СТРОЯК')")
c.execute("INSERT INTO saturday VALUES ('🧠6-я пара (17:00-18:35)🧠', '<----->')")

db.commit()
db.close()