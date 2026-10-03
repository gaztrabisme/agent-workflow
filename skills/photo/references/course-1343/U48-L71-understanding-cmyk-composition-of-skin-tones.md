# Lesson 71 · Understanding CMYK Composition of Skin Tones

Anchor: 1343 · U48 · L71 · 10:59 · https://www.domestika.org/en/courses/1974-course-5-final-touches-and-useful-tips/units/6470-understanding-cmyk-composition-of-skin-tones#course_lesson_19427

## Measuring a skin tone

Anchor: 1343 · U48 · L71 · 00:00–02:10

In this lesson, I’ll measure the CMYK values in skin tones so that I can make an informed edit. Everyone’s skin tone is different, but the color compositions are similar. I’ll use Photoshop’s Info panel to read the CMYK values and Curves for more complex, finely tuned color adjustments.

It can be difficult to measure a person’s skin tone, so these values are guides for editing rather than a single measurement that works for everyone. I have the Info panel in this sidebar. If you cannot find it, open it from the Window menu. Then choose the Color Sampler tool. By default, it uses the same sample size as the Eyedropper tool. As we've discussed before, you should know not to use a point sample. For skin, we want an average: use at least a 5 by 5 average, or an 11 by 11 average.

Choose the sample area carefully. Avoid makeup and very bright highlights. Her forehead might seem like a good place to sample, but it is so bright that it will not contain much color information. I’ll use her chin instead.

![1343 · U48 · L71 · 01:41](frames/U48L71-F0141.00.jpg)

On screen: "Sample Size:" / "Point Sample" / "3 by 3 Average" / "5 by 5 Average" / "11 by 11 Average" / "31 by 31 Average" / "51 by 51 Average" / "101 by 101 Average" [rest omitted]  
Shows: Sample-size menu over the close-up portrait of a light-haired woman; 5 by 5 Average is highlighted, and the sample-size value in the options bar is obscured by the menu.

## Reading the first portrait in CMYK

Anchor: 1343 · U48 · L71 · 02:10–04:05

Photoshop shows RGB values in the Info panel by default: red, green and blue. For skin tones, it is easier to think in cyan, magenta and yellow, so I’ll click the small eyedropper symbol in the panel and change the readout to CMYK. Your result may differ slightly because you may click in a different place. At my chin sample, the values are 11% cyan, 16% magenta and 12% yellow.

These percentages can be misleading because they do not add up to 100. For Caucasian skin, magenta and yellow are typically close, with yellow a little higher. When I say that yellow should be around 10% higher, I do not mean adding ten percentage points to a magenta value of 16% and making yellow 26%. Think of the displayed 16 as a measured amount: ten percent of 16 is 1.6, so yellow would be about 17% or 18%. If the arithmetic is confusing, simply remember that yellow should be slightly higher than magenta.

![1343 · U48 · L71 · 02:26](frames/U48L71-F0226.00.jpg)

On screen: "Sample Size: 11 by 11 Average" / "#1 R: 218 / G: 207 / B: 208" [rest omitted]  
Shows: The color-sampler target is placed on the woman’s chin; the Info panel shows an RGB sample.

![1343 · U48 · L71 · 02:43](frames/U48L71-F0243.00.jpg)

On screen: "C: 11% / M: 16% / Y: 12% / K: 0%" [rest omitted]  
Shows: The sampled chin and its CMYK readout in the Info panel.

## Correcting the first portrait with Curves

Anchor: 1343 · U48 · L71 · 04:05–06:31

The tool for making this adjustment is a Curves layer, which I’ll name “skin tone.” The Targeted Adjustment tool is useful when we want to target a particular brightness value or color. As I move it over the image, a small ball shows the brightness value beneath it. You can see that the bright part of her forehead is close to the top of the range, which is why I avoided sampling there.

To place a point in each color channel, hold Shift and Command on Mac, or Shift and Control on Windows, and click inside the target. It may look as though nothing happened, but Photoshop has placed a point in every channel. Those points correspond to the sampled values in the Info panel.

We are working in the blue channel, although we are thinking about cyan, so the relationship runs in the opposite direction. The main change is to increase yellow. Magenta is 16, so yellow should be around 17 or 18. To increase yellow, subtract blue; I’ll nudge the blue point down with the keyboard arrows and leave it at 17. Looking at the before and after, she looks a little healthier and the skin tone is better.

This is only a guideline because each person has a different skin tone. If you are struggling to get a skin tone right, apply the technique or theory as a starting point, then make further changes from there.

![1343 · U48 · L71 · 04:29](frames/U48L71-F0429.00.jpg)

On screen: "Curves / Preset: Default / RGB / Skin tone" [rest omitted]  
Shows: The named Curves adjustment layer and its Targeted Adjustment tool beside the portrait.

![1343 · U48 · L71 · 04:41](frames/U48L71-F0441.00.jpg)

On screen: "RGB / Input: 238 / Output: 238" [rest omitted]  
Shows: The cursor is over the woman’s bright forehead, with an enlarged inset and a point near the top of the RGB curve.

![1343 · U48 · L71 · 05:41](frames/U48L71-F0541.00.jpg)

On screen: "Blue / Input: 207 / Output: 207 / C: 11% / 11% / M: 16% / 16% / Y: 12% / 12% / K: 0% / 0%" [rest omitted]  
Shows: The blue-channel curve with a sampled point on the portrait and unchanged before-and-after CMYK readouts.

![1343 · U48 · L71 · 06:02](frames/U48L71-F0602.00.jpg)

On screen: "Blue / Input: 207 / Output: 199 / C: 11% / 12% / M: 16% / 16% / Y: 12% / 17% / K: 0% / 0%" [rest omitted]  
Shows: The blue-channel point lowered, with the updated CMYK readout beside the portrait.

## Sampling a second skin tone

Anchor: 1343 · U48 · L71 · 06:31–08:12

Now I’ll look at another image with a very different skin tone. Her forehead is a suitable place to sample, but I’ll keep the point away from the edge. With an 11 by 11 pixel average, sampling too close to the edge would also include some of the background. I’ll set the Info panel to CMYK again.

As a guideline, black skin has a higher cyan value than white skin. Magenta and yellow should be fairly close together, and magenta should be roughly twice the amount of cyan. I’ll add a Curves layer and use the Targeted Adjustment tool as before. Hold Shift and Command, or Shift and Control on Windows, and click once inside the target. Clicking inside it makes the points on the curve correspond to these values.

In the previous image, the readout values did not add up to 100. In this image they add up to well over 100, but each number is a percentage of its own color; they are not parts that must add up to 100%. If the percentages are confusing, think of them simply as amounts of each color.

![1343 · U48 · L71 · 06:37](frames/U48L71-F0637.00.jpg)

On screen: [none]  
Shows: The second portrait: a dark-skinned woman standing in profile, wearing a pale fur-like top and a bright red skirt against a light background.

![1343 · U48 · L71 · 07:11](frames/U48L71-F0711.00.jpg)

On screen: "C: 26% / M: 51% / Y: 80% / K: 7%" [rest omitted]  
Shows: The sampler is placed on the model’s forehead; the Info panel displays its CMYK values.

## Adjusting the second portrait

Anchor: 1343 · U48 · L71 · 08:12–10:59

I’ll start with magenta in the green channel. The point is already selected, so I can nudge it straight away. Magenta is already close to twice the cyan value, but I’ll make it exactly double for accuracy and bring it up to 52. Notice that when I make this change, the yellow value drops from 80 to 79. Changing one color can affect the other readouts, so keep watching all the values as you work.

Next, I’ll reduce yellow in the blue channel. To reduce yellow, add blue, nudging the point up with the arrow keys. Holding Shift moves in steps of ten. For this skin tone, yellow and magenta should be close, with yellow slightly higher. The cyan value has risen a little, but it is still very close to half the magenta value, so I’ll leave it there.

I have added quite a lot of blue. Curves adds light, so the image has become brighter. I could pull down the RGB composite to correct the brightness, but if I only want a color change, I can change the layer blend mode from Normal to Color. Comparing before and after, this is a much better skin tone as a starting point.

It is easy to get used to what is on screen. Sometimes we do not notice a color cast until we start correcting it and compare the before and after. I think this is a better skin tone than the original. I hope you found the lesson useful. For some people this can be a little complicated; for others it can make editing much easier. Some people also find it harder than others to see good-quality skin. In the next lesson, we’ll look at dodge and burn, one of the most important things in retouching.

![1343 · U48 · L71 · 08:42](frames/U48L71-F0842.00.jpg)

On screen: "Green / Input: 127 / Output: 126 / C: 26% / 26% / M: 51% / 52% / Y: 80% / 79% / K: 7% / 7%" [rest omitted]  
Shows: Magenta has been increased in the green channel; the readout shows the small change in yellow as well.

![1343 · U48 · L71 · 09:51](frames/U48L71-F0951.00.jpg)

On screen: "RGB / Input: 255 / Output: 255 / C: 26% / 27% / M: 51% / 53% / Y: 80% / 57% / K: 7% / 7%" [rest omitted]  
Shows: The second portrait after the curve edits, with the RGB composite selected and before-and-after CMYK values in the Info panel.

![1343 · U48 · L71 · 10:11](frames/U48L71-F1011.00.jpg)

On screen: "Color" [rest omitted]  
Shows: The Curves 1 layer is set to Color blending above the portrait; the before-and-after CMYK readouts are visible in the Info panel.
