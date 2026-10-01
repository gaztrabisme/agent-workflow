# Lesson 12 · Notifications, error messages and buttons

Anchor: 798 · U4 · L12 · 14:02 · https://www.domestika.org/en/courses/798-introduction-to-ux-writing/units/5995-write-for-user-experience#course_lesson_18951

## Make notifications contextual and useful

Anchor: 798 · U4 · L12 · 00:00–03:43

It is important to tell people what is happening with your service or digital product, even when they are not using it. This lesson starts with notifications. When you plan the content strategy and write the microcopy for notifications, make sure the information is always contextual and relevant. A notification interrupts someone’s day a little, so it should say what the next action is and where to take it.

Push notifications are common, but there can also be notifications inside an app and notifications supplied by the operating system. The grey pop-ups that appear to come from the operating system are visually separate from the app. Android has the same kind of system-level notification. In the team where I worked, we made a checklist of things to consider. You can print it and use it until you know the questions by heart.

First, ask whether a person is expecting the message or whether it is unexpected and could change their user experience (the captions read “experiencia de su marido”). If they are waiting for a delivery and Amazon tells them when it will arrive, that is expected and fits the moment. If they have a flight scheduled and it is cancelled, an unexpected notification changes their experience and can cause frustration. The tone should vary depending on whether the message is expected, how much the change affects the experience, and how serious it is. A cancelled flight is much more serious than a routine update.

Next, ask whether the message is short and clear, whether it tells the person what to do, and whether the information is useful, contextual, and relevant. Put the user’s benefit at the beginning. Push notifications often have character limits; when a message is too long, it may end in an ellipsis and the rest may not be expandable. The person may never read the rest. As a tip, use roughly the first 35 to 45 characters for the most relevant information. This is called front-loading: put the important part first so it appears on screen. Structure the opening so that a person who sees only the first words can understand the message. Finally, check that the microcopy is consistent with the product’s voice and tone. A checklist helps at first; with practice, you will do it without thinking.

![798 · U4 · L12 · 01:25](frames/U04L12-F0125.00.jpg)

On screen: “/ Mario Ferrer” / “¿La persona está esperando este mensaje o es algo que no se espera y puede cambiar su experiencia de usuario?” [Is the person expecting this message, or is it unexpected and could change their user experience?] / “¿El mensaje es corto y claro?” [Is the message short and clear?] / “domestika.org”  
Shows: The first two questions in a notification-writing checklist.

![798 · U4 · L12 · 02:30](frames/U04L12-F0230.00.jpg)

On screen: “¿Les estás dando información sobre lo que tienen que hacer?” [Are you telling them what they need to do?] / “¿La información es contextual y relevante?” [Is the information contextual and relevant?] [rest omitted]  
Shows: Two more questions in the notification-writing checklist.

![798 · U4 · L12 · 03:25](frames/U04L12-F0325.00.jpg)

On screen: “¿Estás describiendo el beneficio para el usuario al principio del mensaje?” [Are you describing the benefit to the user at the start of the message?] / “¿Mantiene consistencia con la voz y con el tono?” [Does it stay consistent with the product’s voice and tone?] [rest omitted]  
Shows: The final two questions in the notification-writing checklist.

## Show the notification and the next step

Anchor: 798 · U4 · L12 · 03:43–05:50

Let’s look at two push-notification examples I made in Figma. They are useful because they fit the context. The operating system controls details such as how long ago the message arrived; the rest is from the app. This is a wireframe, so it is not exactly how a real notification will look. You can find different templates online depending on the operating system you are designing for.

At the content level, the first example begins with what happened: the reservation is confirmed. Then you can be more personal and give the next piece of information: “See you on Sunday the 8th at 2 p.m.” This tells Marta that the reservation she requested has been confirmed for a particular day and time. She can check that it is the right date and time. If she chose the wrong day or time, she can go back to the app and change or cancel the reservation.

Another kind of notification can help when someone leaves a process unfinished. Marta has selected a day for her reservation but not a time, then closes the app while the session is still open. You can gently and empathetically remind her that she has a reservation in progress and can continue whenever she wants. That information is contextual and relevant. These examples can be built with rectangles or squares and text, as in the rest of the course. They do not need to look flashy; the point is to see how to structure the information.

![798 · U4 · L12 · 04:53](frames/U04L12-F0453.00.jpg)

On screen: “🌮 Tacos” / “Hace 3m” [3m ago] / “Tu reserva está confirmada” [Your reservation is confirmed] / “¡Nos vemos el domingo 8 a las 2pm!” [See you Sunday the 8th at 2 p.m.] / “Tienes una reserva a medias.” [You have a reservation in progress.] / “Puedes continuarla cuando quieras.” [You can continue it whenever you want.] [rest omitted]  
Shows: Two push notifications: one confirms a reservation for Sunday the 8th at 2 p.m.; the other reminds the user to finish a reservation.

## Write error messages that help users recover

Anchor: 798 · U4 · L12 · 05:50–10:41

Digital products and services can have errors, and those need to be communicated. Everyone makes mistakes, often because we are doing other things and our attention is divided. When someone makes a mistake in your app, tell them, but do so with empathy and in context. Put yourself in the other person’s shoes. The tone should change with the situation, and the person should feel that the product is helping them.

Start by telling them the next action and where to take it. Do not just say that there is an error and stop there. Nielsen Norman Group recommends that error messages be direct, clear, kind, precise, constructive, and written in plain language. Most of all, never blame the person using the app. People often feel they have broken something or that something has gone wrong, so communicate calmly: “Don’t worry, it’s okay. Let’s see how we can resolve this.” Help them feel that the problem can be solved.

Work with the product designer so the message appears in the context where the error happened. Explain what happened: “There was an error with your payment” is less useful than saying the card has expired or the card number is wrong. Then give the person options for recovering from the error. The three parts are context, explanation, and ways to recover. Without them, an error feels like a dead end and is frustrating. Sometimes there is no direct solution, but you can still offer alternatives such as returning to the beginning or searching for more information. If someone reads your message and feels they have hit a wall, you need to start again.

Here are three examples for Marta, the app’s prototype user. First, she wants to make a reservation but has mistyped her email, so the app does not recognize it. She may have missed a letter, the “@,” or “.com.” Tell her the reservation has not been made, ask her to check that the email is written correctly and try again, and use a button that says “Review email.” The problem is explained where it happens, and the button gives her a way to fix it.

Second, suppose she tries to reserve a table outside opening hours. You could say, “Try another time.” The tone can be a little playful if it fits the product’s voice: “We want tacos 24/7 too, but we only take reservations from 1 to 11 p.m.” Then give her the option to reserve a table at an available time.

The third case is losing the internet connection. To make a reservation, the user needs an internet connection; the message asks them to reconnect and try again. If the screen has an X and simply closes, the button should say “OK” or “Close,” not “Reserve again,” because it does not perform that action. Try to reduce the number of clicks it takes to get to the next step. Error messages should be contextual and relevant (the captions say “irrelevantes”).

![798 · U4 · L12 · 06:31](frames/U04L12-F0631.00.jpg)

On screen: “Pero hay que decirlo con empatía y de manera contextual.” [But say it with empathy and in context.] [rest omitted]  
Shows: A text slide advises using empathy and context in error messages.

![798 · U4 · L12 · 06:53](frames/U04L12-F0653.00.jpg)

On screen: “Indicar la siguiente acción a realizar y dónde.” [Say what action to take next and where.] [rest omitted]  
Shows: A text slide advises telling users the next action and where to take it.

![798 · U4 · L12 · 07:01](frames/U04L12-F0701.00.jpg)

On screen: “directos” [direct] / “claros” [clear] / “amables” [kind] / “precisos” [precise] / “constructivos” [constructive] / “lenguaje claro” [plain language] [rest omitted]  
Shows: A list of qualities for error messages.

![798 · U4 · L12 · 07:17](frames/U04L12-F0717.00.jpg)

On screen: “Nunca debes culpar a la persona que utiliza tu app.” [Never blame the person using your app.] [rest omitted]  
Shows: A text slide emphasizing that an error message must not blame the user.

![798 · U4 · L12 · 07:41](frames/U04L12-F0741.00.jpg)

On screen: “1.- Dentro del contexto donde sucedió el error.” [1. In the context where the error happened.] [rest omitted]  
Shows: The first part of a three-part error-message structure.

![798 · U4 · L12 · 07:52](frames/U04L12-F0752.00.jpg)

On screen: “2.- Explicar qué ha sucedido.” [2. Explain what happened.] [rest omitted]  
Shows: The second part of the error-message structure.

![798 · U4 · L12 · 08:00](frames/U04L12-F0800.00.jpg)

On screen: “3.- Dar opciones para recuperarse del error.” [3. Give options for recovering from the error.] [rest omitted]  
Shows: The third part of the error-message structure.

![798 · U4 · L12 · 08:29](frames/U04L12-F0829.00.jpg)

On screen: “Que no sea callejón sin salida, si no hay solución al error, dales la opción de volver al inicio o buscar más información.” [Do not let it become a dead end; if there is no solution to the error, give them the option to return to the beginning or search for more information.] [rest omitted]  
Shows: A slide recommends offering a way back or a way to find more information when an error has no direct solution.

![798 · U4 · L12 · 08:54](frames/U04L12-F0854.00.jpg)

On screen: “Tu reserva aún no está hecha” [Your reservation has not been made yet.] / “Por favor revisa que tu email esté bien escrito y vuelve a intentarlo.” [Please check that your email is written correctly and try again.] / “Revisar email” [Review email.] [rest omitted]  
Shows: An email-entry error explains that the reservation was not made and offers a button to review the address.

![798 · U4 · L12 · 09:54](frames/U04L12-F0954.00.jpg)

On screen: “Intenta en otro horario” [Try another time.] / “Nosotros también queremos tacos 24/7 pero solo reservamos de 1 a 11 pm.” [We want tacos 24/7 too, but we only take reservations from 1 to 11 p.m.] / “Reservar mesa” [Reserve a table.] [rest omitted]  
Shows: An opening-hours error explains when reservations are available and offers a button to reserve a table.

![798 · U4 · L12 · 10:15](frames/U04L12-F1015.00.jpg)

On screen: “No hay internet” [There is no internet connection.] / “Para reservar necesitas conexión a internet. Conéctate e inténtalo de nuevo.” [To reserve, you need an internet connection. Connect and try again.] / “Ok” [OK.] [rest omitted]  
Shows: An internet-connection error tells the user what is needed and provides an “OK” button.

## Make buttons say what will happen

Anchor: 798 · U4 · L12 · 10:41–14:02

Now for what I find hardest in UX writing: buttons. They are small and have only a few words, which leaves very little space to help and guide the person. Localization can make the wording longer in some languages and break the layout, so you have to work hard on button copy. Always state the action the button will perform, and make sure the action it names is the action that will actually happen.

If a button cannot do anything because of a technical limitation, or the screen is only a notification, give the user an “OK” or “Close” message. It can work like the X at the top of the screen: the system has given the information, and the user can acknowledge it and close it. Although the product is a conversation in service of an end goal, buttons are some of the few places where the user actually interacts. Think of a button as the user’s response to what the system has said.

Keep buttons short, use verbs that describe actions, and use the active voice (*voz activa*). People tend to read titles and buttons most, according to the studies I mentioned earlier about F-shaped reading. If a screen’s title and button make it clear what is happening, where the user is, and what action to take, the app becomes much easier to use. You can then make more room for body copy, but if the title and button are clear, you have already won half the battle.

When you need two buttons, use clear pairs such as “Yes / No” or “Accept / Cancel.” Some apps try to be playful with button labels, but then people may not know what action they are taking. Keep the options clear and make sure the person can predict what will happen when they choose either one. Finally, stay consistent with the product’s voice and tone. That is how you practise structuring text for a digital product or service. In the next lesson, I’ll talk about accessibility, diversity, and localization.

![798 · U4 · L12 · 11:39](frames/U04L12-F1139.00.jpg)

On screen: “Indica la acción a realizar.” [State the action to be performed.] [rest omitted]  
Shows: A text slide advises naming the button’s action.

![798 · U4 · L12 · 12:30](frames/U04L12-F1230.00.jpg)

On screen: “Mantenlos cortos, usa verbos y voz activa.” [Keep them short, use verbs, and use the active voice.] [rest omitted]  
Shows: A text slide with three tips for button labels.

![798 · U4 · L12 · 12:39](frames/U04L12-F1239.00.jpg)

On screen: “Las 2 cosas que las personas más leen:” [The two things people read most:] / “Títulos y botones” [Titles and buttons] [rest omitted]  
Shows: A text slide identifies titles and buttons as the two most-read elements.

![798 · U4 · L12 · 13:09](frames/U04L12-F1309.00.jpg)

On screen: “Usa dicotomías” [Use binary pairs.] / “Si - No” [Yes – No] [rest omitted]  
Shows: A text slide recommends clear yes-or-no button pairs.

![798 · U4 · L12 · 13:37](frames/U04L12-F1337.00.jpg)

On screen: “Sé consistente.” [Be consistent.] [rest omitted]  
Shows: A text slide advises consistency.

### Key points (derived)

- Notifications should fit the context, lead with the user’s benefit, and make the next action clear.
- Error messages should explain what happened and help users recover without blaming them.
- Button labels should be short, active, consistent, and accurate about the result of a tap.
