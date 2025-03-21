<div align="center">

![GitHub downloads](https://img.shields.io/github/downloads/halynakov/evently-management-system/total?label=Загальна%20кількість%20завантажень&amp;style=for-the-badge)

![GitHub followers](https://img.shields.io/github/followers/halynakov?style=social?&amp;label=Споглядачі)
![GitHub forks](https://img.shields.io/github/forks/halynakov/evently-management-system?style=social?&amp;label=Форки)
![GitHub stars](https://img.shields.io/github/stars/halynakov/evently-management-system?style=social?&amp;label=Зірки)

### <img src="https://raw.githubusercontent.com/halynakov/evently-management-system/refs/heads/main/Evently/frontend/static/frontend/assets/images/logo-menu-2x.png"/>

</div>

## 📋Зміст пояснювальної записки

1. [Розгортання](##⚙️Розгортання)
2. [Відеопрезентація](##🎞Відеопрезентація)
3. [Ліцензування](##⚖️Ліцензування)
4. [Автори](##✒️Автори)

## ⚙️Розгортання

> [!WARNING]  
><details><summary></summary>
> Це керівництво зі власного розгортання проекту було сформовано з урахуванням, де-факто, відсутності встановленої потрібної версії Python'у на локальній машині, а також в цілому для машин що оперуються системою <strong>Windows 10/11</strong>, але й на Unix-подібних ОС це керівництво повинно бути корисним, але з деякими незначними нюансами.
></details>

<a id="step-0"></a>

0. Для початку клонуйте за допомогою "**Git**" репозиторій проекту у зручне для Вас місце на вашому пристрої, або ж, якщо у Вас немає "**Git**", то просто завантажте репозиторій у вигляді zip-архіву й потім розархівуйте його вміст у, знову ж таки, зручну для Вас папку, опісля чого відкрийте у цій самій теці PowerShell/cmd для подальшого успішного встановлення й базового налаштування середовища для розгортання проекту.

<a id="step-1"></a>

1. Тепер перевірте яку версію Python встановлено на вашій машині, та чи встановлено яку-небудь версію взагалі, за допомогою наступної універсальної консольної команди для PowerShell/cmd:
    ```powershell
    python --version
    ```
> [!IMPORTANT]  
><details><summary></summary>
> Якщо опісля відпрацювання команди Ви виявили те, що у Вас взагалі не встановлено Python, або ж у Вас встановлено версію відмінну від версії "<strong>3.12.5</strong>", за допомогою відповідних виведень до консолі, то Вам необхідно перейти до кроку під номером <a href="#step-2"><strong>2</strong></a> цього керівництва, якщо ж Python є й він навіть тієї версії що потрібно, то Ви можете одразу ж перейти до кроку <a href="#step-3"><strong>3</strong></a>.
></details>

<a id="step-2"></a>

2. Завантажте з офіційного сайту Python файли для встановлення останнього на вашу машину [за наступним посиланням](https://www.python.org/downloads/release/python-3125/#:~:text=Full%20Changelog-,Files,-Version) та, на всяк випадок, опісля поетапно розписаної процедури встановлення поверніться до кроку [**1**](#step-1).

<a id="step-3"></a>

3. Далі використовуючи спеціальну систему керування програмними пакетами Python, цебто ["**pip**"](https://pypi.org/project/pip/), Вам необхідно встановити менеджер з керування залежностями під назвою - ["**Poetry**"](https://python-poetry.org/). Зробити це можна увівши до раніше відкритої консолі наступну універсальну команду:
    ```powershell
    pip install poetry
    ```
> [!TIP]  
><details><summary></summary>
> Якщо у Вас вже встановлено "<strong>Poetry</strong>", то цей крок можна пропустити, бо для розгортання проекту підійде будь-яка актуальна версія цього ПЗ, навіть досить стара. До прикладу, у проекті було використано, де-факто, найновішу станом на березень 2025 року версію, а саме - "<strong>2.1.1</strong>".
></details>

<a id="step-4"></a>

4. Далі Вам потрібно активувати раніше встановлений "**Poetry**" за допомогою консолі, аби він міг автоматично підтягнути усі необхідні для коректних розгортання й подальшої роботи <u>**залежності**</u>. Задіяння менеджеру треба провести за допомогою спеціальної універсальної для PowerShell/cmd консольної команди:
    ```powershell
    poetry install
    ```

    <a id="step-5"></a>

> [!TIP]  
><details><summary></summary>
> Якщо у Вас встановлено версію "<strong>Poetry</strong>" старшу за "<strong>2.0.0</strong>" <strong><u>не включно</u></strong>, то Ви можете хоробро пропустити цей крок й одразу ж перейти до кроку <a href="#step-7"><strong>7</strong></a>, бо потрібна команда у Вас буде працювати й без усіляких додаткових, так би мовити, хитрощів.
></details>

5. Опісля вдалого автоматичного підтягування залежностей за допомогою "**Poetry**" Вам необхідно ввести до Вашої консолі наступну команду, аби переконатися у тому, що у склонованому Вами репозиторії присутній скрипт активації віртуального середовища у поточній оболонці "**Poetry**":
    ```powershell
    poetry env activate
    ```

> [!IMPORTANT]  
><details><summary></summary>
> Наступна консольна команда не активує віртуальне середовище у поточній оболонці "<strong>Poetry</strong>", тому у кроці <a href="#step-6"><strong>6</strong></a> цього керівництва Ви встановите офіційний плагін від розробників "<strong>Poetry</strong>", аби у Вас з'явилась можливість запустити це саме віртуальне середовище котре потрібне для подальшої роботи.
></details>

<a id="step-6"></a>

6. Тепер Вам потрібно встановити офіційний плагін від розробників "**Poetry**", котрий надасть можливість активувати віртуальне середовище у поточній оболонці раніше неодноразово згаданого "**Poetry**". Для цього дійства нам знадобиться наступна консольна команда:
    ```powershell
    poetry self add poetry-plugin-shell
    ```

<a id="step-7"></a>

7. Як тільки все буде готово, Ви зможете запустити віртуальне середовище у поточній оболонці "**Poetry**" за допомогою наступної консольної команди:
    ```powershell
    poetry shell
    ```

<a id="step-8"></a>

8. Далі Вам варто для зручності за допомогою консольної команди під номером [**1**](#first-command) перейти до відповідної теки раніше скопійованого Вами репозиторію, де розташовується далі вкрай необхідний файл під назвою - "**manage.py**"; опісля виконання першої команди Вам одразу ж треба буде задіяти [**другу**](#second-command) консольну команду, котра як раз нарешті й активує локальний сервер, аби закінчити розгортання сайту й аби у Вас з'явилася неілюзорна можливість власноруч протестувати проект. Ось самі команди:
    <a id="first-command"></a>
    ```powershell
    cd .\Evently\
    ```
    <a id="second-command"></a>
    ```powershell
    python manage.py runserver
    ```

> [!WARNING]  
><details><summary></summary>
> Якщо у Вас не вдається запустити сервер з-за занятості порту <strong>"8000"</strong>, тоді Вам треба подивитися чим цей же самий порт зайнятий й, відповідно, опісля виявлення вивільнити його, також Ви можете змінити порт задіяний у проекті, але ми наполегливо <strong>не рекомендуємо</strong> це робити.
></details>

<a id="step-9"></a>

9. Врешті-решт Ви отримаєте повідомлення про те, що сервер запрацював, й аби перейти вже до самого сайту, Вам необхідно або скопіювати наведене там посилання (а саме "**http://127.0.0.1:8000/**", якщо Ви, звісно ж, нічого не змінювали) й вставити його до будь-якого браузеру, або ж Ви можете, з-за відповідної можливості, просто при утриманому пальці на кнопці Ctrl клацнути ЛКМ (<kbd>Ctrl</kbd> + <kbd>ЛКМ</kbd>) по цьому ж самому посиланню, й у Вас відкриється Ваш браузер за замовчуванням з цим самим сайтом.

> [!NOTE]  
><details><summary></summary>
> Якщо будуть якісь труднощі з розгортанням, або ж це керівництво не відповіло на Ваші запитання щодо процесу розгортання, тоді запрошуємо Вас до вкладки <a href="https://github.com/halynakov/evently-management-system/issues/new/choose"><strong>"Issues"</strong></a> нашого репозиторію, де ми зможемо Вам з усім допомогти, або ж на усе відповісти, відповідно.
></details>

## 🎞Відеопрезентація

<div align="center">
<a href="https://drive.google.com/file/d/1GKVrLe44x1iIwlwMZ-_WJ3FJ71lxI1BH/view">
    <img src="https://drive.google.com/thumbnail?id=1GKVrLe44x1iIwlwMZ-_WJ3FJ71lxI1BH" width="600"/>
</a>
</div>

## ⚖️Ліцензування

Проект поширюється на умовах ліцензії [MIT](https://raw.githubusercontent.com/twbs/bootstrap/refs/heads/main/LICENSE).

## ✒️Автори

<!-- Incorrect display
<a href="https://github.com/halynakov" style="display: flex; align-items: center; gap: 10px; padding: 8px; border: 1px solid #ddd; border-radius: 8px; text-decoration: none; background-color: #f9f9f9; transition: background-color 0.2s, transform 0.2s;" onmouseover="this.style.backgroundColor='#e8f4ff'; this.style.transform='scale(1.05)'" onmouseout="this.style.backgroundColor='#f9f9f9'; this.style.transform='scale(1)'">

  <img src="https://avatars.githubusercontent.com/u/109976190?s=48&v=4" width="96" height="96" style="border-radius: 0%; border: 2px solid #0366d6;" title="Visit halynakov's GitHub profile" alt="halynakov's Avatar"/>

  <div style="display: flex; flex-direction: column;">
    <strong style="color: #0366d6;">@halynakov</strong>
    <span style="font-size: 14px; color: #333;">🚀 Lead Backend Developer</span>
    <span style="font-size: 12px; color: #666;">⏳ 2 years of experience</span>
    <span style="font-size: 12px; color: #666;">📌 Passionate about open-source & AI</span>
  </div>
</a>

<br/>
-->

[![Contributors](https://contrib.rocks/image?repo=halynakov/evently-management-system)](https://github.com/halynakov/evently-management-system/graphs/contributors)

### [@gubanna11 (aka Губа Ганна)](https://github.com/gubanna11)

<a href="https://github.com/gubanna11">
  <img src="https://avatars.githubusercontent.com/u/83699357?s=96" title="Visit gubanna11's GitHub profile" alt="gubanna11's Avatar"/>
</a>

><details>
>  <summary><b>БІОГРАФІЯ</b></summary>
>  <table>
>    <tbody>
>      <tr>
>        <td>🎓 <strong>НТУ "ХПІ"</strong></td>
>      </tr>
>      <tr>
>        <td>⚙️ <strong>Backend</strong></td>
>      </tr>
>      <tr>
>        <td>👩‍💻⚙️ <strong>Team Lead</strong></td>
>      </tr>
>    </tbody>
>  </table>
></details>

### [@halynakov (aka Галина Ковалевська)](https://github.com/halynakov)

<a href="https://github.com/halynakov">
  <img src="https://avatars.githubusercontent.com/u/109976190" width="96" height="96" title="Visit halynakov's GitHub profile" alt="halynakov's Avatar"/>
</a>

><details>
>  <summary><b>БІОГРАФІЯ</b></summary>
>  <table>
>    <tbody>
>      <tr>
>        <td>🎓 <strong>НТУ "ХПІ"</strong></td>
>      </tr>
>      <tr>
>        <td>⚙️ <strong>Backend</strong></td>
>      </tr>
>      <tr>
>        <td>👩‍💻 <strong>Розробник</strong></td>
>    </tbody>
>  </table>
></details>

### [@olyaakov (aka Ольга Ковалевська)](https://github.com/olyaakov)

<a href="https://github.com/olyaakov">
  <img src="https://avatars.githubusercontent.com/u/125313311" width="96" height="96" title="Visit olyaakov's GitHub profile" alt="olyaakov's Avatar"/>
</a>

><details>
>  <summary><b>БІОГРАФІЯ</b></summary>
>  <table>
>    <tbody>
>      <tr>
>        <td>🎓 <strong>НТУ "ХПІ"</strong></td>
>      </tr>
>      <tr>
>        <td>⚙️ <strong>Backend</strong></td>
>      </tr>
>      <tr>
>        <td>💾 <strong>Відповідальний за бази даних</strong></td>
>      <tr>
>        <td>👩‍💻 <strong>Розробник</strong></td>
>      </tr>
>    </tbody>
>  </table>
></details>

### [@darrdasha (aka Дар'я Савченко)](https://github.com/darrdasha)

<a href="https://github.com/darrdasha">
  <img src="https://avatars.githubusercontent.com/u/122937754?s=96" title="Visit darrdasha's GitHub profile" alt="darrdasha's Avatar"/>
</a>

><details>
>  <summary><b>БІОГРАФІЯ</b></summary>
>  <table>
>    <tbody>
>      <tr>
>        <td>🎓 <strong>НТУ "ХПІ"</strong></td>
>      </tr>
>      <tr>
>        <td>⚙️ <strong>Backend</strong></td>
>      </tr>
>      <tr>
>        <td>👩‍💻 <strong>Розробник</strong></td>
>      </tr>
>    </tbody>
>  </table>
></details>

### [@sofieke-L (aka Софія Лошкарьова)](https://github.com/sofieke-L)

<a href="https://github.com/sofieke-L">
  <img src="https://avatars.githubusercontent.com/u/162575380?s=96" title="Visit sofieke-L's GitHub profile" alt="sofieke-L's Avatar"/>
</a>

><details>
>  <summary><b>БІОГРАФІЯ</b></summary>
>  <table>
>    <tbody>
>      <tr>
>        <td>🎓 <strong>НТУ "ХПІ"</strong></td>
>      </tr>
>      <tr>
>        <td>♿ <strong>Frontend</strong></td>
>      </tr>
>      <tr>
>        <td>🎨🧩 <strong>UX/UI-дизайнер</strong></td>
>      </tr>
>    </tbody>
>  </table>
></details>

### [@hryhoriikorsun (aka Григорій Корсунь)](https://github.com/sofieke-L)

<a href="https://github.com/hryhoriikorsun">
  <img src="https://avatars.githubusercontent.com/u/102456972?s=96" title="Visit hryhoriikorsun's GitHub profile" alt="hryhoriikorsun's Avatar"/>
</a>

><details>
>  <summary><b>БІОГРАФІЯ</b></summary>
>  <table>
>    <tbody>
>      <tr>
>        <td>🎓 <strong>ХНУРЕ</strong></td>
>      </tr>
>      <tr>
>        <td>👨‍💻🎨 <strong>Full-stack</strong></td>
>    </tbody>
>  </table>
></details>

### [@sviatomishl (aka Арсентій Більдін)](https://github.com/sviatomishl)

<a href="https://github.com/sviatomishl">
  <img src="https://avatars.githubusercontent.com/u/115322932?s=96" title="Visit sviatomishl's GitHub profile" alt="sviatomishl's Avatar"/>
</a>

><details>
>  <summary><b>БІОГРАФІЯ</b></summary>
>  <table>
>    <tbody>
>      <tr>
>        <td>🎓 <strong>НТУ "ХПІ"</strong></td>
>      </tr>
>      <tr>
>        <td>♿ <strong>Frontend</strong></td>
>      </tr>
>      <tr>
>        <td>🎨🧩 <strong>Молодший UX/UI-дизайнер</strong></td>
>      </tr>
>      <tr>
>        <td>🔍 <strong>Тестувальник</strong></td>
>      </tr>
>    </tbody>
>  </table>
></details>
