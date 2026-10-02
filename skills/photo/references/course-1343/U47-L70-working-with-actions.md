# Lesson 70 · Working with Actions

Anchor: 1343 · U47 · L70 · 11:18 · https://www.domestika.org/en/courses/1974-course-5-final-touches-and-useful-tips/units/6469-working-with-actions#course_lesson_19426

## Actions as a workflow tool

Anchor: 1343 · U47 · L70 · 00:00–01:59

1343 · U47 · L70 · 00:00–01:59

One of my favorite things in Photoshop is writing actions to help with my workflow. Actions are small scripts: you program Photoshop to perform tasks automatically. They are easier to make than they sound. I will show you how to create your own actions and install actions made by someone else. As you become more efficient in Photoshop, a solid, strategic workflow matters, and actions are an important part of mine.

Open the Actions panel. Photoshop comes with a set called Default Actions. I do not know what they are for and find them pretty pointless, so I deleted them. I create a new folder, which Photoshop calls a set, and name it Retouching.

When I work with many images, I like to create an action called Workflow that structures the image's layers. The images differ, so I will not always use the same layers, but the overall structure and buildup of layers and groups are very similar. For client work, keeping layers in the same places and giving them the same names also looks professional and makes it easier to talk through the file together.

![1343 · U47 · L70 · 01:08](frames/U47L70-F0108.00.jpg)

On screen: "Actions" [rest omitted]  
Shows: The source studio photograph is open in Photoshop; the Actions panel is open and empty after the default actions have been removed.

## Create and record the layer structure

Anchor: 1343 · U47 · L70 · 02:00–03:59

1343 · U47 · L70 · 02:00–03:59

Click the plus button at the bottom of the Actions panel to create an action and call it Workflow. I do not tend to use function keys. They are meant to create keyboard shortcuts, but the computer's operating system always overrides Photoshop's shortcuts, so they quite often do not work. I also give the action a color. I choose green as an indication that this is the first thing I do, and will show what the color does later.

Press Record. I typically start many images with a couple of layers for cloning. That may not be the first step in every workflow, but I want those layers above the Background, so that is where this action begins. I name one layer Clean up, add another and call it Details. I could add more layers now; for the moment, the point is to establish the structure.

Put the two layers in a group. Select both by Command-clicking on a Mac or Control-clicking on Windows. Alternatively, select the first layer and Shift-click the last to select a whole range. Drag the selected layers down to create a group, and call it Clone. On top of that group, add a Curves adjustment layer and name it Brightness. Put a point in the center of the Brightness curve; this is also recorded in the action. The first point changes it: input is 127 and output is 129.

![1343 · U47 · L70 · 02:38](frames/U47L70-F0238.00.jpg)

On screen: "Retouching" / "New Action" / "Name: Workflow" / "Set: Retouching" / "Function Key: None" / "Color: Green" / "Record" / "Cancel" [rest omitted]  
Shows: The New Action dialog names Workflow in the Retouching set, leaves the function key unset, and assigns green; the source photo remains open.

![1343 · U47 · L70 · 03:14](frames/U47L70-F0314.00.jpg)

On screen: "Details" / "Clean up" / "Background" / "Make layer" / "Set current layer" / "Make layer" / "Set current layer" [rest omitted]  
Shows: The Details and Clean up layers sit above Background; the Actions panel lists the recorded layer-creation steps.

![1343 · U47 · L70 · 03:35](frames/U47L70-F0335.00.jpg)

On screen: "Clone" / "Select layer \"Clean up\"" / "Make Group" [rest omitted]  
Shows: The two retouching layers have been placed in a collapsed Clone group above Background.

![1343 · U47 · L70 · 03:45](frames/U47L70-F0345.00.jpg)

On screen: "Curves" / "Brightness" / "Input:" / "Output:" / "Make adjustment layer" / "Select RGB channel" [rest omitted]  
Shows: A Curves adjustment layer named Brightness has been added above the Clone group; its curve is still a straight diagonal.

![1343 · U47 · L70 · 03:55](frames/U47L70-F0355.00.jpg)

On screen: "Input: 127" / "Output: 129" [rest omitted]  
Shows: The selected point on the Brightness curve has input 127 and output 129.

## Build an adjustment stack

Anchor: 1343 · U47 · L70 · 04:00–05:55

1343 · U47 · L70 · 04:00–05:55

That changes the curve, which I do not want, so I nudge the point with the arrow keys until input and output match. The middle of the tonal range is 128, so that is a good place to keep it.

Add another Curves layer for color, but do not add any points because color adjustments depend on the image. Add a third curve for contrast, also without points because contrast depends a lot on the image itself. I also tend to use Vibrance. I delete the “1” so it is not called Vibrance 1. I often work with Hue/Saturation, but rarely use the saturation part, so I delete that part of the name and call the layer Hue.

Shift-click the last layer and put the adjustment layers into a group called Adjustments. Finally, add a Roadmap layer and perhaps a Notes layer. Notes are useful when working with clients, as mentioned earlier. Put those two layers into a group called Notes. I typically start my workflow with Brightness.

![1343 · U47 · L70 · 04:09](frames/U47L70-F0409.00.jpg)

On screen: "Input: 128" / "Output: 128" [rest omitted]  
Shows: The selected center point on the Brightness curve has equal input and output values of 128.

![1343 · U47 · L70 · 05:45](frames/U47L70-F0545.00.jpg)

On screen: "Notes" / "Adjustments" / "Select layer \"Roadmap\"" [rest omitted]  
Shows: The finished layer stack has collapsed Notes, Adjustments, and Clone groups above Background.

## Stop and test the action

Anchor: 1343 · U47 · L70 · 05:56–07:39

1343 · U47 · L70 · 05:56–07:39

Select Brightness and press Stop. It is very important to remember to stop recording here. If you make a mistake while making an action and then undo it, the action records both the mistake and the undo. I will show how to edit an action and remove mistakes.

After stopping, revert the image from the History panel by going to the top of its history. Select the action's title and press Play. Fingers crossed, I should now have a Clone group with its two layers. The Brightness layer is also there and is selected because it was selected when I started. The Clone group is closed, and so is the Notes (captions: “nodes”) group, which is typically how I want them.

One thing that surprises me is that the curve points were not recorded. I am not sure whether I made a mistake, Adobe made a mistake, or Photoshop no longer allows points to be put into Curves in an action. It used to be possible, and I think that is useful. We will have to find out in a later Photoshop update.

![1343 · U47 · L70 · 07:11](frames/U47L70-F0711.00.jpg)

On screen: "Hue" / "Vibrance" / "Contrast" / "Colo" [rest omitted]  
Shows: The adjustment layers are visible above the expanded Clone group; the Brightness curve has no added point.

## Edit which steps play

Anchor: 1343 · U47 · L70 · 07:40–09:32

1343 · U47 · L70 · 07:40–09:32

Editing an action is simple. In the Actions panel, the check mark on the left means that a step is active. If you no longer want part of the action to play—for example, if you do not want it to create one of the layers—find that step and uncheck it. An unchecked step gives the action title a red check mark, indicating that the unchecked step will not play.

The box on the right has a different purpose. If a step opens a dialog, enabling this box makes the action stop at that dialog so you can change its value. Press OK and the action continues. This is useful. We are not looking at it now, but I will show it later in the course. We will also record a few actions together during the course.

![1343 · U47 · L70 · 08:25](frames/U47L70-F0825.00.jpg)

On screen: "Retouching" / "Workflow" [rest omitted]  
Shows: The enlarged Actions panel inset shows red check marks beside the Retouching set and Workflow action, with check marks and empty boxes beside their recorded steps.

![1343 · U47 · L70 · 08:53](frames/U47L70-F0853.00.jpg)

On screen: "Make Group" / "Set current layer" / "Make layer" / "Set current layer" / "Make layer" / "Set current layer" / "Select layer \"Roadmap\"" [rest omitted]  
Shows: The Actions panel is scrolled through the recorded steps, with their check marks and dialog boxes visible.

Everything in the action is recorded in the Actions panel, so its step list can look messy. This is an editing layout for actions, and it lets you play an action from the list. I recommend using this layout when creating or editing actions.

## Run actions as buttons

Anchor: 1343 · U47 · L70 · 09:33–11:18

1343 · U47 · L70 · 09:33–11:18

For normal work in Photoshop, use Button Mode: each action appears as a button.

Delete all the layers, then press the Workflow button to play the action. The button is green, which is why I chose a color when creating the action. I love actions and use them all the time on my computer; I have many that I use regularly in Photoshop. They can do complex things such as build a layer structure, or simple repeated tasks such as sharpening images. Whenever we see a need for an action during this course, we will make one together. You will practise creating them and end up with useful actions of your own.

I hope you enjoyed learning to write an action. If you think you will do something more than a few times, I recommend writing an action for it. In the next lesson, we will learn to edit skin tones and start looking at CMYK composition in images.

![1343 · U47 · L70 · 10:08](frames/U47L70-F1008.00.jpg)

On screen: "Workflow" [rest omitted]  
Shows: In Button Mode, Workflow appears as a green button in the Actions panel; the organized layer stack remains visible.
