# Lesson 08 · To move graphics 2. We go deep into the animation curves

Anchor: 503 · U2 · L08 · 13:46 · https://www.domestika.org/en/courses/503-introduction-to-motion-design-and-animation-curves-in-after-effects/units/2010-cheering-in-after-effects-with-style#course_lesson_7405

## Convert linear keyframes to curves

Anchor: 503 · U2 · L08 · 00:00–01:14

Real control over animation comes from mastering the Graph Editor and animation curves (*curvas de animación*). The lesson also covers animating Position by separating its X and Y dimensions.

The starting keyframes are linear. In a preview, the animation stops abruptly. Select them and press F9 to change them to eased keyframes; their icons become bow-tie shapes rotated on their sides. Preview again and the animation is smoother. That gives us the raw material to begin adjusting the curves.

![503 · U2 · L08 · 00:08](frames/U02L08-F0008.00.jpg)

On screen: "#dmstkh79" / "A mover gráficos 2." [Moving graphics 2.] / "Nos adentramos" [We go deeper] / "hasta el fondo" [into the depths] / "en las curvas de animación" [into the animation curves]  
Shows: Purple lesson title card with a geometric shape icon.

![503 · U2 · L08 · 00:56](frames/U02L08-F0056.00.jpg)

On screen: [none]  
Shows: A selected purple circle and its scale keyframes in the timeline after easing.

## Open and frame the Graph Editor

Anchor: 503 · U2 · L08 · 01:14–03:23

Open the Graph Editor. We will focus on the buttons that are useful for making animations rather than learning every button. If the animated property is not selected, its curve will not appear. If the curve disappears, select the property or the layer.

The Fit All Graphs to View button fits the graph into the timeline so it is easier to work with. To select one or more keyframes, I recommend clicking and dragging; that is cleaner and less likely to move them accidentally. Double-clicking the animated property selects all the keyframes for it. Selecting a keyframe shows its Bezier handles, because F9 made these eased keyframes. You can turn them back into linear keyframes with the linear-keyframe option, then restore the curves with F9 or the curve button.

![503 · U2 · L08 · 01:20](frames/U02L08-F0120.00.jpg)

On screen: "Graph Editor" [rest omitted]  
Shows: The purple circle is visible above the timeline, with the Graph Editor control under the cursor.

![503 · U2 · L08 · 02:03](frames/U02L08-F0203.00.jpg)

On screen: [none]  
Shows: The scale curve is fitted into the Graph Editor.

![503 · U2 · L08 · 02:44](frames/U02L08-F0244.00.jpg)

On screen: [none]  
Shows: The Value Graph is open with two eased keyframes and their handles selected.

## Choose the Value Graph or Speed Graph

Anchor: 503 · U2 · L08 · 03:23–04:33

After Effects has two ways to display curves: the Value Graph (*gráfico de valores*) and the Speed Graph (*gráfico de velocidad*). I will show both, but I recommend using only the Value Graph. Its representation is compatible with animation programs such as Cinema 4D and other industry-standard tools. The Speed Graph is almost unique to After Effects. You can use it if it works for you, but that keeps the workflow inside After Effects. I prefer the more standard Value Graph. If you see the mountain-like Speed Graph, switch to the Value Graph so we are working in the same mode.

The graph-type menu is in the button bar at the bottom of the Graph Editor, just to the right of the eye icon. Open that dropdown to choose Edit Value Graph or Edit Speed Graph.

![503 · U2 · L08 · 03:54](frames/U02L08-F0354.00.jpg)

On screen: "Auto-Select Graph Type" / "Edit Value Graph" / "Edit Speed Graph" / "Show Reference Graph" / "Show Audio Waveforms" / "Show Layer In/Out Points" / "Show Layer Markers" / "Show Graph Tool Tips" / "Show Expression Editor" / "Allow Keyframes Between Frames" [rest omitted]  
Shows: The graph-type menu open over the Scale Value Graph.

![503 · U2 · L08 · 04:24](frames/U02L08-F0424.00.jpg)

On screen: "Edit Value Graph" / "Edit Speed Graph" [rest omitted]  
Shows: The graph-type menu open over a Value Graph with a rising curve.

## Zoom and move around the graph

Anchor: 503 · U2 · L08 · 04:33–06:22

Now we can work on the curves. Use the zoom control and Fit All Graphs to View so the graph has enough space. Do not work with the graph cramped. A control that is on by default fits the graph’s height to the displayed curve. If you turn it off, hold Control and use the mouse wheel to zoom vertically. If the graph moves out of view, hold the spacebar, click, and drag to pan around the editor.

You can keep automatic fitting enabled, or turn it off and use Control plus the wheel for vertical zoom, then the spacebar to move around. I switch between those ways of working. The default height-fitting option is useful. Work with enough space, use zoom and Fit All to frame the graph, and turn off automatic fitting only when you need more vertical detail. On a Mac, use Command with the wheel.

![503 · U2 · L08 · 04:41](frames/U02L08-F0441.00.jpg)

On screen: [none]  
Shows: The Graph Editor is zoomed to show the scale curve and its handles.

## Read the curve and adjust its handles

Anchor: 503 · U2 · L08 · 06:22–09:12

The horizontal axis represents time, and the vertical axis represents the value being changed. In the displayed graph, Scale starts at 100%, dips to about 70%, and then rises to 180%. Steeper slopes mean faster animation. A flatter curve, almost parallel to the horizontal axis, means slower animation.

Pulling a handle to the left makes this part faster and makes the approach smoother or slower. We can adjust another curve as well, exaggerating the handles so the keyframes are very smooth and the in-between movement is very fast. Preview the result with the spacebar. The animation continues in a loop, and we can adjust the curve while it previews.

Be careful when pulling a Bezier handle vertically: that changes the animation’s value as well as its timing or speed. That can create a bounce if it is what you want. In this example, the intended final Scale value is 180%, but pulling past it reaches about 185%. If you do not want that overshoot, keep the handles from changing the value. To move keyframes, leave the Graph Editor and move them in the timeline; that is cleaner and avoids changing the curves. Then return to the Graph Editor to continue editing the curves.

![503 · U2 · L08 · 06:41](frames/U02L08-F0641.00.jpg)

On screen: [none]  
Shows: The selected scale curve rises from a low value to a higher value, with the circle enlarged at the later keyframe.

![503 · U2 · L08 · 07:24](frames/U02L08-F0724.00.jpg)

On screen: [none]  
Shows: A scale handle has been adjusted, changing the curve’s timing near the selected keyframe.

![503 · U2 · L08 · 08:17](frames/U02L08-F0817.00.jpg)

On screen: "Scale" / "185.1, 185.1 %" [rest omitted]  
Shows: The scale curve overshoots its final value, with the pointer over the raised handle.

## Add curve keyframes and edit Position

Anchor: 503 · U2 · L08 · 09:12–11:57

The Pen tool shortcut is G. When its icon appears over the curve, clicking there adds another keyframe. Exit the Graph Editor and you can see that the same tool adds keyframes there too. Press V to return to the cursor and work with the new keyframe. Preview the result. A point added to the curve is another keyframe.

Now make a new composition with a background shape layer. Select all the keyframes and hold Alt to speed them up until the timing is about right. Press F9, enter the Graph Editor, and click Fit All Graphs to View. Position has a special case when we edit it in the Value Graph: its Bezier handles do not appear. We must separate the dimensions—X and Y—to access those handles. Click Separate Dimensions. This can make the curves untidy; in this example, because the animation is only in X, I can delete the Y keyframes by clicking that property’s stopwatch. Then work on the curves as needed. To animate Position in the Value Graph, remember to separate its dimensions. Select Position and click the same button to separate them; click it again to return X and Y to one combined property.

![503 · U2 · L08 · 09:31](frames/U02L08-F0931.00.jpg)

On screen: [none]  
Shows: A new keyframe is added to the scale curve with the Pen tool.

![503 · U2 · L08 · 10:14](frames/U02L08-F1014.00.jpg)

On screen: "Comp 1" [rest omitted]  
Shows: A newly created wide composition with a white background.

![503 · U2 · L08 · 10:51](frames/U02L08-F1051.00.jpg)

On screen: [none]  
Shows: A red circle is selected in the new wide composition, ready for the Position example.

![503 · U2 · L08 · 10:57](frames/U02L08-F1057.00.jpg)

On screen: "Position" [rest omitted]  
Shows: The red circle is selected in the Composition viewer with its horizontal motion path visible; the Graph Editor below shows a red curve and a green horizontal line.

## Use the Speed Graph for Position if preferred

Anchor: 503 · U2 · L08 · 11:57–13:46

I still recommend the Value Graph, but because separating Position’s dimensions can be awkward, you may find the Speed Graph more convenient for Position animation. Select the keyframes and convert them to curves. In the Speed Graph, manipulating handles creates a steep section and a valley near the keyframe. A steep slope means high speed; a value nearly parallel to the horizontal axis means the movement eases. Adjust the handles, then preview. I do not prefer this graph because it is less compatible with other animation software, but if you get used to it and prefer it for Position, use it; the resulting animation can be just as good.

With this, you should be able to work confidently in the Graph Editor and make smooth animations. We have now covered animation curves in depth. The next lesson is about rendering and video output formats.

![503 · U2 · L08 · 12:26](frames/U02L08-F1226.00.jpg)

On screen: [none]  
Shows: A red circle and its horizontal motion path appear above the Speed Graph.

![503 · U2 · L08 · 13:34](frames/U02L08-F1334.00.jpg)

On screen: [none]  
Shows: The red circle is at the right end of its horizontal path; three speed peaks are visible below.

### Key points (derived)

- F9 makes linear keyframes easier to work with in the Graph Editor.
- In the Value Graph, time runs horizontally and property value vertically; steep segments are fast and flat segments are slow.
- For Position curves in the Value Graph, separate X and Y dimensions to access their handles.
