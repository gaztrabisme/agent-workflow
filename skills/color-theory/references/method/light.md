# Light: where most color in an image comes from

Reader: an agent deciding the light of an image before choosing colors, or checking that the colors obey the light. Sources: [1140 L06](../course/U02-L06-understand-the-light-to-be-able-to-illuminate.md), [1140 L11](../course/U03-L11-rhythm-and-balance.md), [1140 L18](../course/U04-L18-bonus-solving-common-color-problems.md), [1560 L05–L15](../course-1560/U02-L05-soft-light-vs-hard-light.md).

## Three principles

The teacher's recap states them as three principles. (1140 · U2 · L06 · 17:46–19:52)

1. **Lighting is a very blurred reflection of the surroundings.**
   - A mirror sphere shows the sky, the floor and its neighbours sharply.
   - A matte sphere shows the same things, blurred into a gradient: sky color on top, floor color below.

   (1140 · U2 · L06 · 03:15–05:03)
2. **An object's color has two parts.**
   - **Local color**: what is painted on the object, also called its texture.
   - **Specularity**: how smooth and reflective the material is. It runs from broken, rough highlights (brick, hair) to mirror.

   (1140 · U2 · L06 · 05:03–06:42)
3. **Light bounces many times.** Every lit surface acts as a colored, diffuse light source for its neighbours, so local color is almost never seen pure. (1140 · U2 · L06 · 08:13–10:43, 1140 · U2 · L06 · 10:43–13:51)

## Direct and indirect light

| | Direct | Indirect (diffuse) |
|---|---|---|
| Rays | Parallel, one direction | Scattered, from everywhere (through clouds, off surfaces) |
| Terminator (the line where light stops reaching the form) | Sharp | Soft, porous |
| Cast shadow | Hard | Blurred |

(1140 · U2 · L06 · 06:42–08:13)

## Build a digital-painting light pass

Course 1560 treats light quality as a continuum from soft ambient illumination to hard direct light. Set the source direction and softness first; overcast light stays diffuse, while direct sun can coexist with sky ambient light. (1560 · U2 · L05 · 01:04–03:43, 1560 · U2 · L05 · 07:27–08:18, 1560 · U2 · L05 · 08:41–09:17)

1. **Set exposure.** Decide how the scene's light and shadow range will fit the painting's available range, and which information must remain visible. (1560 · U2 · L06 · 00:08–01:48, 1560 · U2 · L06 · 01:49–04:41)
2. **Place the source and choose its quality.** A cloudy scene has broad soft illumination; a sunny scene has a strong directional source and clearer cast shadows. (1560 · U2 · L05 · 03:44–04:46, 1560 · U3 · L09 · 01:40–04:48, 1560 · U3 · L10 · 00:26–01:53, 1560 · U3 · L10 · 01:53–03:39)
3. **Separate local color from the light pass.** Establish the drawing and base colors on simple forms before adding the scene's light and shadow. (1560 · U2 · L07 · 03:25–05:24)
4. **Add ambient and secondary sources by priority.** In a night scene, the blue ambient field and warm practical lights can coexist; multiple sources need an order so the dominant one remains legible. (1560 · U3 · L11 · 01:44–02:55, 1560 · U3 · L11 · 03:39–04:58, 1560 · U3 · L12 · 04:00–05:54, 1560 · U3 · L12 · 05:54–07:25)
5. **Add reflected color, then material cues.** Bounce is strongest on nearby surfaces and falls away with distance; finish with specular reflection or translucency only where the material supports it. (1560 · U3 · L13 · 06:30–07:57, 1560 · U2 · L06 · 13:28–18:26, 1560 · U4 · L14 · 05:08–05:58)

These steps are a **derived** order assembled from the preparation and scene demonstrations, not a quoted fixed sequence. (derived from 1560 · U2 · L06 · 00:08–01:48, 1560 · U2 · L06 · 01:49–04:41, 1560 · U2 · L07 · 03:25–05:24, 1560 · U3 · L09 · 01:40–04:48, 1560 · U3 · L13 · 06:30–07:57)

### Lighting situations used for practice

| Situation | Lighting decision | Source |
|---|---|---|
| Sunny exterior | Protect the bright range, keep a directional key, and let nearby surfaces pick up colored bounce. | 1560 · U3 · L09 · 01:40–04:48, 1560 · U3 · L13 · 06:30–07:57 |
| Cloudy exterior | Use broad, cool-white ambient illumination with soft shadows and restrained directional contrast. | 1560 · U3 · L10 · 00:26–01:53, 1560 · U3 · L10 · 01:53–03:39 |
| Night | Let cool ambient light carry the scene and warmer lamps act as local sources; keep secondary rim light subordinate. | 1560 · U3 · L11 · 01:44–02:55, 1560 · U3 · L11 · 03:39–04:58 |
| Colored room | Track each source's direction and strength; nearby surfaces can pick up colored bounce, while small sources fall off quickly. | 1560 · U3 · L12 · 02:23–04:00, 1560 · U3 · L12 · 04:00–05:54, 1560 · U3 · L12 · 05:54–07:25 |

## How colored light changes a sphere

The teacher changes one variable at a time on a sphere. (1140 · U2 · L06 · 10:43–13:51)

1. **White sphere on a blue floor:** the lower half turns blue-grey.
2. **Red sphere, blue floor, white light:** the lit side stays light red. The side facing the floor drifts toward purple.
3. **Same, under yellow light:** the lit side moves to salmon-yellow. The local red survives only where no bounce or light color reaches.

Perfectly white light is rare, so "the local color of objects is almost never intrinsic". (1140 · U2 · L06 · 10:43–13:51)

## Daylight rule used in the course image

- **Direct light:** overhead sun between 12 and 3 o'clock, slightly yellow.
- **Shadows:** lit by the sky, so they are cooler.
- **The course image:** on a yellow ground, the shadow shifts from yellow to green.
- **Why it matters for harmony:** the yellowish light pulls every lit color toward the ground's yellow, and the cool shadow ties the ground to the sky and trees.

(1140 · U3 · L11 · 10:39–12:31, 1140 · U3 · L11 · 12:31–13:55)

## Light as a harmonizer

- Bounced light justifies putting a color from one block into its neighbour. Examples:
  - a red floor tints an animal's fur;
  - the ground's orange lights characters' lower halves.

  (1140 · U3 · L10 · 00:00–01:51)
- See [harmony-bridges.md](harmony-bridges.md).

## Style is how much the light is simplified

- **Graphic light** reduces lighting to local color, one light tone, one shadow tone and a cast shadow. (1140 · U2 · L06 · 13:51–15:40)
- A stylization scale runs from total abstraction to realistic 3D rendering, where bounces are visible, such as orange light from the chest under a chin:
  1. Bart Simpson, Hellboy, anime;
  2. comic hatching;
  3. soft-gradient cartoon;
  4. painted comic covers;
  5. 3D render.

  (1140 · U2 · L06 · 13:51–15:40, 1140 · U2 · L06 · 15:40–17:46)
- **Derived decision:** decide the level of stylization before painting light (derived: the lesson demonstrates a chosen "relatively graphic" treatment using a terminator, specular highlight, bounce light and a glow; 1140 · U2 · L07 · 05:48–07:32).

## Check: color coherent with the light

This is Problem 6.

- **The failure:** a warm light is established, but an object's lit side is painted cooler than its shadow. (1140 · U4 · L18 · 10:26–12:20)
- **The rule:**
  - lit sides take the light's temperature;
  - shadows take the ambient temperature;
  - the object shows an evolution from warm to cold across its form.

  A cold purple object under warm light is warm pink on the lit side and cooler toward the shadow. A cyan light source pushes its side toward cyan. (1140 · U4 · L18 · 10:26–12:20)
- Decide the lighting early. "The clearer our decisions are, the easier they are to follow." (1140 · U4 · L18 · 10:26–12:20)

Practice the teacher sets:
- Build a small still life.
- Light it from 3 directions and photograph each.
- Paint each photo, matching the colors and values.

See [1140 U02](../course/U02-unit.md) and [1560 U02](../course-1560/U02-unit.md), [U03](../course-1560/U03-unit.md) and [U04](../course-1560/U04-unit.md).
