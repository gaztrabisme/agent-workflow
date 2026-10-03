# Lesson 13 · Accessibility, diversity and localization

Anchor: 798 · U4 · L13 · 17:49 · https://www.domestika.org/en/courses/798-introduction-to-ux-writing/units/5995-write-for-user-experience#course_lesson_18952

## See how a screen reader uses the computer

Anchor: 798 · U4 · L13 · 00:00–04:28

Remember that there are many kinds of users, including people with different abilities. As a UX writer, your responsibility is to make sure the experiences you design with your team are accessible and take that diversity into account. Small changes can have a big impact.

There are many different people who may use your app, so give extra attention to diversity when you design content. I’ll show an example because it is interesting to see how a blind person can use a computer if you have never used screen-reader software (*software de lector de pantalla*).

![798 · U4 · L13 · 00:48](frames/U04L13-F0048.00.jpg)

On screen: “/ Mario Ferrer” / “Muchas personas diferentes pueden usar tu app.” [Many different people can use your app.] / “domestika.org”  
Shows: A dark text slide says that many different people can use the app.

![798 · U4 · L13 · 00:53](frames/U04L13-F0053.00.jpg)

On screen: “Foto: Wayhome Studio” [Photo: Wayhome Studio] [rest omitted]  
Shows: Four people sit with a phone or tablet in their hands.

The example video asks how a blind person uses a computer. The answer is through the keyboard, a program with a voice, and keyboard commands. Each keyboard key has an equivalent to a mouse function. The left mouse button corresponds to the Enter key, the large key. The captions say “barra de borrar” for the Backspace key. The context menu—the right mouse button—has the Application key as its keyboard equivalent, one of the keys people often overlook at the bottom of the keyboard.

With voice synthesis, whether human or robotic, and keyboard commands, a person can move around the computer screen, open windows, and move through desktop elements. To go to the desktop in the demonstration, the speaker presses Windows+N and then moves among the items with the arrow keys. He presses Enter to open an item and Alt+F4 to close a window. He can move through the system tray, where volume, internet connection, and other information appear.

A person can also browse the internet, use word-processing software, make presentations, use spreadsheets and chat programs, and use social networks and other everyday tools. Many keyboard commands recur and perform different functions. Ctrl+P prints a document, Ctrl+C copies, and Ctrl+V pastes. Most people do not know many of the other commands that support blind people in their daily work (the captions read “junto a estas mujeres”).

As you can see, people using a screen reader usually do not navigate with a mouse. This is where microcopy matters for accessibility. The small commands have to be clear, useful, and concise because the machine tells the person where each section is very quickly. The words have to explain what is happening and make it clear. Small wording changes can make an app, website, service, or other digital product more accessible.

![798 · U4 · L13 · 01:08](frames/U04L13-F0108.00.jpg)

On screen: “Lector de Pantalla: ¿Cómo usa una persona ciega un computador?” [Screen Reader: How does a blind person use a computer?] [rest omitted]  
Shows: An embedded video shows a blind computer user and displays the tutorial title.

![798 · U4 · L13 · 02:03](frames/U04L13-F0203.00.jpg)

On screen: [illegible] [rest omitted]  
Shows: A close-up shows a finger pressing the large Enter key on the keyboard.

![798 · U4 · L13 · 02:12](frames/U04L13-F0212.00.jpg)

On screen: [illegible]  
Shows: A young man in a computer room explains the screen-reader demonstration.

![798 · U4 · L13 · 02:16](frames/U04L13-F0216.00.jpg)

On screen: [illegible] [rest omitted]  
Shows: A close-up shows a finger pressing the Application key near the bottom of the keyboard.

![798 · U4 · L13 · 03:09](frames/U04L13-F0309.00.jpg)

On screen: “¡NO COMER!” [NO EATING!] / “MIENTRAS TRABAJA EN LA BIBLIOTECA” [WHILE WORKING IN THE LIBRARY.]  
Shows: A young man uses a keyboard at a computer workstation.

![798 · U4 · L13 · 03:11](frames/U04L13-F0311.00.jpg)

On screen: [none]  
Shows: The tutorial shows a Windows file window open on the computer screen.

## Give users the information before the action

Anchor: 798 · U4 · L13 · 04:28–08:09

Screen-reader users move through content in blocks rather than taking in the whole screen at once. They go piece by piece because a screen reader cannot give them a complete picture of everything on the screen. It reads the title, image, subtitle, body copy, and the rest of the information. Navigation moves up and down, then left and right. When you design the content, think about that order, and speak with the developers so they set the accessibility navigation keys in the same way. People can then move block by block.

Give people the information they need before they take an action. You may be able to see the whole screen and know what will happen, but a person navigating one block at a time may not know a password’s minimum requirements. They could hear “name, field; surname, field; email, field; password, field,” enter a password that has fewer than eight characters and lacks uppercase letters or numbers, and only then get an error. That can become a frustrating loop because they were never told the requirements.

Ideally the screen reader says “password,” gives the minimum password requirements, and then says “field.” The form shown in the lesson does not have to be arranged that way visually, although that would be ideal. If the form already exists, work with development to set the navigation order in the code so the screen reader reads the label, help text, and then the field. In the example, it would announce “password,” “minimum 8 characters and include uppercase letters and numbers,” and then the field.

The same applies to an item below the fields, such as a terms-and-conditions checkbox. If the user fills everything in, creates a password, and tries to create an account without checking the box, the app will prevent them and show an error. Tell the user they need to check it before they press the button. Put the information earlier on screen if possible; if the form is already built, make sure the screen reader reaches it earlier in the code.

![798 · U4 · L13 · 05:20](frames/U04L13-F0520.00.jpg)

On screen: “Cursos recomendados” [Recommended courses] / “UX: Usabilidad y Experiencia de Usuario” [UX: Usability and User Experience] / “Introducción al Desarrollo Web Responsive con HTML y CSS” [Introduction to Responsive Web Development with HTML and CSS] / “Branded content y content curation para tu marca personal” [Branded content and content curation for your personal brand] / “Storytelling aplicado a marcas” [Storytelling applied to brands] / “Foto: Wayhome Studio” [Photo: Wayhome Studio] [rest omitted]  
Shows: A recommended-courses page with four course cards, each showing an image, title, and other information.

![798 · U4 · L13 · 05:51](frames/U04L13-F0551.00.jpg)

On screen: “arriba” [up] / “abajo” [down] / “izquierda” [left] / “derecha” [right] [rest omitted]  
Shows: A text slide lists the four navigation directions.

![798 · U4 · L13 · 06:57](frames/U04L13-F0657.00.jpg)

On screen: “Nombre” [First name] / “Apellido” [Last name] / “Email” [Email] / “Contraseña” [Password] / “Mínimo 8 caracteres e incluir mayúsculas y números.” [At least 8 characters and include uppercase letters and numbers.] / “Crea tu cuenta” [Create your account] / “Aceptar Términos y condiciones” [Accept Terms and Conditions] / “Foto: Wayhome Studio” [Photo: Wayhome Studio] [rest omitted]  
Shows: A sign-up form with labels, password requirements, a create-account button, and a terms-and-conditions checkbox.

![798 · U4 · L13 · 07:17](frames/U04L13-F0717.00.jpg)

On screen: “Etiqueta” [Label] / “Texto de ayuda” [Help text] / “Campo” [Field] [rest omitted]  
Shows: A text slide gives the screen-reader order for form elements.

## Use alternative text and clear labels

Anchor: 798 · U4 · L13 · 08:09–11:23

Spend a little time on alternative text (*texto alternativo*). It helps with accessibility and with slow internet connections, so it is useful in both situations. Imagine a screen from a vintage toy store with a robot image. If the page does not load, or if the screen reader encounters an image, it will say “image” and continue with the text. Add alternative text in brackets: “Image: toy robot.” That tells the user what the image is without a lengthy description. Use alternative text for images that communicate something and are part of the structure of your message.

You have seen icons like these in many places. Without alternative text, the screen reader may announce “link,” “image,” “icon,” or “button.” If it reads five different icons as “button, button, button, button, button,” the user will not know what each one does or where it goes. The alternative text should describe the destination, not the appearance of the image. The examples could be pinned posts, notifications, home, alerts, and profile. Make it clear where a tap or click will take the person.

Icons can be difficult to identify on a small screen, even for people without disabilities, and the same icon can mean something different to different people. If you can, add a small visible label. If you cannot, at least give the icon a clear alternative text that tells the user where it leads.

Avoid putting text inside an image. A screen reader will not recognize it as text. Use live text (*texto en vivo*) separate from the image, so the screen reader can read: “404. This page is not available. Return to the main menu.”

Finally, be clear. Sometimes we want to be playful, but consider a progress bar that says “Wrapping.” A screen reader may only read “Wrapping,” especially if the progress bar is an image that is only partly filled. Add another short line: “We’re finishing your order.” These are basic examples from a small area of accessibility—people who use screen readers—but they can make a big difference. Keep accessibility in mind when you start designing content, and talk with design and development so all three groups understand it from the beginning and can make these small changes.

![798 · U4 · L13 · 08:36](frames/U04L13-F0836.00.jpg)

On screen: “Juguetes Vintage” [Vintage Toys] / “Redescubre los mejores juguetes de tu infancia” [Rediscover the best toys from your childhood.] [rest omitted]  
Shows: A vintage-toy store card features a pixel-style robot and short promotional copy.

![798 · U4 · L13 · 08:57](frames/U04L13-F0857.00.jpg)

On screen: “[imagen: robot de juguete]” [image: toy robot] [rest omitted]  
Shows: The same store card shows the robot’s alternative text in the image area.

![798 · U4 · L13 · 09:58](frames/U04L13-F0958.00.jpg)

On screen: [rest omitted]  
Shows: Five icons are shown in a row: a pin, alarm clock, home, bell, and person.

![798 · U4 · L13 · 10:29](frames/U04L13-F1029.00.jpg)

On screen: “404” / “Esta página no está disponible” [This page is not available.] / “Vuelve al menú inicial” [Return to the main menu.] [rest omitted]  
Shows: An error page displays live text and a link back to the main menu.

![798 · U4 · L13 · 11:20](frames/U04L13-F1120.00.jpg)

On screen: “Envolviendo...” [Wrapping...] / “Estamos terminando tu orden.” [We’re finishing your order.] [rest omitted]  
Shows: A partially filled progress bar appears beneath two lines of order-status text.

## Localize for the culture and the language

Anchor: 798 · U4 · L13 · 11:23–13:18

As well as accessibility and diversity, UX writers need to think about localization (*localización*). Most digital products and services are available in several languages and countries. Localization is more complex than translation: it means designing for other cultures and languages and making sure that what you write makes sense in that cultural context.

The language may be the same while the words differ. In Spain, a computer is called an “ordenador”; in Mexico, it is a “computadora.” Use the local word in the interface so it does not sound strange.

![798 · U4 · L13 · 12:34](frames/U04L13-F1234.00.jpg)

On screen: “· Ordenador” [Computer] / “· Computadora” [Computer] / “Foto:” [Photo:] / [illegible] [rest omitted]  
Shows: Two side-by-side laptop photos are labeled with the Spanish terms used for a computer in Spain and Mexico.

Work closely with the localization team. Do not send only the text strings (*strings*; the captions read “SARIs”); they need context. They need to know where the text appears, what the next action is, and where the person came from. Ideally, share the flow so they can see where the text will be, what else is on the screen, and whether an image or another element, such as a map or calendar, supports it. Tell them the previous steps the user took and where the experience should take them next.

![798 · U4 · L13 · 12:56](frames/U04L13-F1256.00.jpg)

On screen: “Incluye el flujo como referencia” [Include the flow as a reference.] [rest omitted]  
Shows: A text slide recommends sharing the product flow with the localization team.

![798 · U4 · L13 · 13:15](frames/U04L13-F1315.00.jpg)

On screen: “Foto: Álvaro Reyes” [Photo: Álvaro Reyes] / [rest omitted]  
Shows: A hand marks a path across wireframes and diagrams on a wall.

## Keep a shared glossary of common terms

Anchor: 798 · U4 · L13 · 13:18–14:20

![798 · U4 · L13 · 13:56](frames/U04L13-F1356.00.jpg)

On screen: “Bonjour!” [Hello!] / “Hello!” / “Ciao!” [Hello!] / “Hola!” [Hello!] / “Foto: iStock” [Photo: iStock] [rest omitted]  
Shows: Four people hold signs with greetings in French, English, Italian, and Spanish.

To avoid reinventing the wheel, work with the localization team to create a glossary of common terms. If a term appears frequently in your app, you do not need to translate it from scratch every time. Keep the original language—for example, Spanish—and the term as it appears in each of the app’s ten languages.

This helps in two ways. It saves time and localization costs. It also lets you test longer words while designing. Spanish may already look long, but German tends to use longer words. Put the German version into your wireframe and see whether it will be too long. If it is, look for alternatives before the localization process has to start over for that term. A shared term bank or glossary makes the work easier for both sides.

## Give the localization team a CopyDocs page

Anchor: 798 · U4 · L13 · 14:20–16:09

Another useful tool is CopyDocs, which is used quite a bit; the people at Dropbox do it well. It can be a simple page with the project name at the top. Start with relevant documentation, such as the company’s voice-and-tone guide. People doing localization are often external and do not have the context you have, so include earlier user research, data showing what works and what does not, related projects, and whether this work is part of something larger. The more information and context you provide, the better.

The next section should contain style notes. A word that is formal in Spanish might be too formal or too informal in German. Explain why you chose these words and why the language needs to sound this way from your perspective as a UX writer. These notes help the localization team stay as close as possible to the original version.

Include a screenshot of the screen with its context, and add notes if you can. Also include the different versions of the microcopy you tried (the captions read “microcopio”). You may believe that the final version is the best one, but if the localization team says it does not fit their language, an earlier version may work. All that context and information helps a lot.

![798 · U4 · L13 · 16:07](frames/U04L13-F1607.00.jpg)

On screen: “Proyecto” [Project] / “Documentos relevantes” [Relevant documents] / “Notas sobre estilo” [Style notes] / “Captura de pantalla con contexto” [Screenshot with context] / “Versiones del microcopy” [Microcopy versions] [rest omitted]  
Shows: A CopyDocs page has fields for project documentation, style notes, a contextual screenshot, and microcopy versions.

## Explain the value of UX writing and finish the course

Anchor: 798 · U4 · L13 · 16:09–17:49

Before we finish, keep in mind that many product-design teams have never worked with someone dedicated full time to UX writing. The role is relatively new, and there are not many specialists yet, especially in Spanish-speaking countries. Look for them on Twitter or LinkedIn and ask questions; people tend to be very kind. Think about how you can help companies understand the value of this work. When more companies recognize the role’s value, there will be more job opportunities for everyone.

If you start working with a product team that does not understand the role, help them see what you can contribute and how you can work together. From your perspective as a UX writer, think about how to solve their design problems. The idea is for everyone to help each other provide a better user experience.

We have covered a little of everything, and you have had to put these ideas into practice. As a UX writer, you have an extra responsibility to take account of people who are different and help them have a better experience. This is the end of the course. I hope you found the information interesting and useful, and that you can use it in your projects and work as a UX writer. Please stay for the next lesson, where I will summarize the concepts we have covered.

### Key points (derived)

- Screen-reader content needs a predictable order, useful labels, and the information users need before an action.
- Alternative text and concise, clear wording help people understand images, icons, errors, and progress.
- Give localization teams context, shared terminology, and rationale so the experience fits other cultures and languages.
