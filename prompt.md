## Task: Generate Metadata from HTML + Raw Filename

```text
You are an expert front-end engineer and UI systems designer.

You will be given:
1. A raw HTML document (may include inline or embedded CSS)
2. The original filename (e.g., "0xnihilism_pretty-fireant-33.html") - Mostly Random

Your task is to analyze both inputs to extract structured metadata in JSON format. 

Your task is to output a JSON with:

### Output JSON Structure

{{
  "description": "<Two-line vivid explanation of what the component looks like and does.>",
  "production_filename": "<A suggested filename in camelCase or kebab-case identifier usable as component filename name.>",
  "colors": ["#HEX1", "#HEX2", ...],
  "tags": ["tag1", "tag2", ...]
}}

Use filename (generally randomly generated may not relate to the content), code content, css styles etc as context for style hints.


You must deduce:

### OUTPUT FIELDS:

1. **description** (string): A human-readable sentence describing what this component does or looks like. Focus on appearance (e.g., glassmorphism, 3D, neumorphism, brutalism), animation (hover, click, pulsate, gradient), and purpose (button, card, loader, etc.).

2. **production_filename** (string): A clean, production-friendly identifier in camelCase or kebab-case format (e.g., `darkGlassyButton` or `neumorphic-input-card`). Base this on your understanding of the style, type, and behavior of the component.

3. **colors** (array of strings): Extract all dominant or unique HEX color codes from the HTML/CSS. Return only valid hex codes (e.g., `#ff5733`, `#121212`). Sort them by visual prominence. Always include # before a hex value number

4. **tags** (array of strings): Valid tags for the given description and code from below list of tags: button,card,loader,rounded,dark,simple,minimal,white,animation,blue,form,black,input,hover,switch,animated,icon,hover effect,modern,gradient,shadow,text,centered,gray,checkbox,3d,purple,minimalist,green,neumorphism,tooltip,material design,red,label,radio,bold,minimalistic,circle


### RULES:
- Do not include colors like `transparent`, `inherit`, or `currentColor`.
- Always base your decisions on the visual appearance and component purpose.
- Use the filename as context if it has themes (e.g., "fireant" or "glass", etc.)

Respond with valid JSON only. Do not include extra text.

---

### EXAMPLES:

#### INPUT:
```html
<!-- HTML Snippet -->
<button class="glass-btn">Click me</button>
<style>
  .glass-btn {
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid #ffffff;
    backdrop-filter: blur(10px);
    color: #ffffff;
  }
</style>

<!-- Filename -->
0xSarthak_hungry-penguin-30.html
```

#### OUTPUT:
```json
{
  "description": "A glassmorphism-styled button with semi-transparent background, frosted blur effect, and subtle white border that creates a modern, translucent appearance.",
  "production_filename": "glassButtonBlur",
  "colors": ["#ffffff", "#000000"],
  "tags": ["button", "modern", "minimal", "hover", "animation"]
}
```

---

#### INPUT:
```html
<button class="cta">
  <span>Contact Us &nbsp;</span>
  <svg viewBox="0 0 13 10" height="10px" width="15px">
    <path d="M1,5 L11,5"></path>
    <polyline points="8 1 12 5 8 9"></polyline>
  </svg>
</button>
<style>
.cta {
  position: relative;
  margin: auto;
  padding: 11.5px 18px;
  transition: all 0.2s ease;
  border: 3px solid #552da8;
  border-radius: 50px;
  background: #552da8;
  cursor: pointer;
}
.cta:before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  display: block;
  border-radius: 50px;
  background: white;
  width: 45px;
  height: 45px;
  transition: all 0.8s ease;
}
.cta span {
  position: relative;
  font-family: Montserrat;
  font-size: 18px;
  color: white;
  font-weight: 400;
  letter-spacing: 0.05em;
}
.cta svg {
  position: relative;
  top: 0;
  margin-left: 10px;
  fill: none;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke: white;
  stroke-width: 2;
  transform: translateX(-5px);
  transition: all 0.5s ease;
}
.cta:hover:before {
  width: 100%;
  background: #1c1c1c;
}
.cta:hover svg {
  transform: translateX(0);
  transition: all 2s ease;
}
.cta:active {
  transform: scale(0.95);
  transition: all 2s ease;
}
</style>

<!-- Filename -->
0x-Sarthak_hungry-penguin-30.html
```

#### OUTPUT:
```json
{
  "description": "A purple rounded button with animated hover effect that reveals a dark background from right to left, featuring an arrow icon that moves on hover and a subtle scale animation on click.",
  "production_filename": "animatedPurpleButton",
  "colors": ["#552da8", "#ffffff", "#1c1c1c"],
  "tags": ["button", "hover", "rounded", "animated", "purple", "modern"]
}
```

---

#### INPUT:
```html
<div class="notification">
  <span>Congratulatioins Champion!</span>
  <div id="level">
    <div class="one">↑</div>
    <div id="lvl">Level 10</div>
    <div class="one">↑</div>
  </div>
</div>
<style>
@keyframes ud {
  0% {
    transform: translateY(-1px);
    opacity: 0;
  }
  50% {
    transform: translateY(-5px);
    opacity: 1;
  }
  100% {
    transform: translateY(-1px);
    opacity: 0;
  }
}
.notification {
  width: 250px;
  height: 60px;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 14px;
  padding: 5px 15px;
  text-align: center;
  box-shadow: 2px 2px 0px 1px rgba(255, 0, 0, 0.5) inset, 
  -2px -2px 0px 1px rgba(255, 0, 0, 0.8) inset,
  0px 2px 5px 0px rgba(0, 0, 0, .25);
}
#lvl {
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-size: 20px;
}
.notification > span {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 1px;
}
#level {
  display: flex;
  justify-content: center;
  margin-top: 5px;
  gap: 5px;
}
.one {
  display: inline-block;
  font-size: 25px;
  line-height: 25px;
  animation: ud 1s ease-in-out infinite;
  color: rgba(255, 0, 0, 0.95);
}
</style>

<!-- Filename -->
ActiveIceDigital_fuzzy-fly-47.html
```

#### OUTPUT:
```json
{
  "description": "A semi-transparent dark notification card with red inset shadows and animated upward arrows, designed to display achievement messages with a level indicator.",
  "production_filename": "achievementNotificationCard",
  "colors": ["#000000", "#ff0000", "#ffffff"],
  "tags": ["card", "dark", "animation", "red", "centered", "modern"]
}
```

---

#### INPUT:
```html
<div class="container"></div>
<style>
.container {
  --color1: rgb(179, 255, 226);
  --color2: rgb(39, 0, 148);
  width: 100%;
  height: 100%;
  background-image: linear-gradient(45deg, var(--color1) 25%, transparent 25%, transparent 75%, var(--color1) 75%, var(--color1)),
                    linear-gradient(45deg, var(--color2) 25%, var(--color1) 25%, var(--color1) 75%, var(--color2) 75%, var(--color2));
  background-size: 95px 15px;
  background-position: 0 0, 135px 135px;
}
</style>

<!-- Filename -->
aadium_hard-swan-77.html
```

#### OUTPUT:
```json
{
  "description": "A geometric pattern background with alternating mint green and deep blue colors creating a checkerboard-like duotone effect with diagonal stripes.",
  "production_filename": "geometricDuotonePattern",
  "colors": ["#b3ffe2", "#270094"],
  "tags": ["pattern", "blue", "green", "gradient", "minimal"]
}
```

---

#### INPUT:
```html
<section class="add-card page">
  <form class="form">
    <label for="name" class="label">
      <span class="title">Card holder full name</span>
      <input
        class="input-field"
        type="text"
        name="input-name"
        title="Input title"
        placeholder="Enter your full name"
      />
    </label>
    <label for="serialCardNumber" class="label">
      <span class="title">Card Number</span>
      <input
        id="serialCardNumber"
        class="input-field"
        type="number"
        name="input-name"
        title="Input title"
        placeholder="0000 0000 0000 0000"
      />
    </label>
    <div class="split">
      <label for="ExDate" class="label">
        <span class="title">Expiry Date</span>
        <input
          id="ExDate"
          class="input-field"
          type="text"
          name="input-name"
          title="Expiry Date"
          placeholder="01/23"
        />
      </label>
      <label for="cvv" class="label">
        <span class="title"> CVV</span>
        <input
          id="cvv"
          class="input-field"
          type="number"
          name="cvv"
          title="CVV"
          placeholder="CVV"
        />
      </label>
    </div>
    <input class="checkout-btn" type="button" value="Checkout" />
  </form>
</section>
<style>
.form {
  background: #0c0f14;
  box-shadow: 0px 187px 75px rgba(0, 0, 0, 0.01),
    0px 105px 63px rgba(0, 0, 0, 0.05), 0px 47px 47px rgba(0, 0, 0, 0.09),
    0px 12px 26px rgba(0, 0, 0, 0.1), 0px 0px 0px rgba(0, 0, 0, 0.1);
  width: 320px;
  display: flex;
  flex-direction: column;
  gap: 15px;
  padding: 20px;
  position: relative;
  border-radius: 25px;
}
.form .label {
  display: flex;
  flex-direction: column;
  gap: 5px;
  height: -moz-fit-content;
  height: fit-content;
}
.form .label:has(input:focus) .title {
  top: 0;
  left: 0;
  color: #d17842;
}
.form .label .title {
  padding: 0 10px;
  transition: all 300ms;
  font-size: 12px;
  color: #8b8e98;
  font-weight: 600;
  width: -moz-fit-content;
  width: fit-content;
  top: 14px;
  position: relative;
  left: 15px;
  background: #0c0f14;
}
.form .input-field {
  width: auto;
  height: 50px;
  text-indent: 15px;
  border-radius: 15px;
  outline: none;
  background-color: transparent;
  border: 1px solid #21262e;
  transition: all 0.3s;
  caret-color: #d17842;
  color: #aeaeae;
}
.form .input-field:hover {
  border-color: rgba(209, 121, 66, 0.5);
}
.form .input-field:focus {
  border-color: #d17842;
}
.form .split {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  gap: 15px;
}
.form .split label {
  width: 130px;
}
.form .checkout-btn {
  margin-top: 20px;
  padding: 20px 0;
  border-radius: 25px;
  font-weight: 700;
  transition: all 0.3s cubic-bezier(0.15, 0.83, 0.66, 1);
  cursor: pointer;
  font-size: 20px;
  font-weight: 500;
  display: flex;
  align-items: center;
  border: none;
  justify-content: center;
  fill: #fff;
  color: #fff;
  border: 2px solid transparent;
  background: #d17842;
  transition: all 200ms;
}
.form .checkout-btn:active {
  scale: 0.95;
}
.form .checkout-btn:hover {
  color: #d17842;
  border: 2px solid #d17842;
  background: transparent;
}
</style>

<!-- Filename -->
3bdel3ziz-T_helpless-wasp-32.html
```

#### OUTPUT:
```json
{
  "description": "A dark-themed credit card form with floating labels that animate on focus, featuring orange accent colors, rounded input fields with hover and focus states, and a checkout button with hover animation that changes from solid to outlined style.",
  "production_filename": "darkCreditCardForm",
  "colors": ["#0c0f14", "#21262e", "#8b8e98", "#d17842", "#aeaeae", "#ffffff"],
  "tags": ["form", "dark", "input", "material design", "animation", "hover", "modern", "rounded"]
}
```

---

#### INPUT:
```html
<div class="card">
  <div data-text="The Eye of Providence" class="title">
    The Eye of Providence
  </div>
  <div class="eye-of-providence">
    <div class="triangle"></div>
    <div class="eye">
      <div class="eyelid"></div>
      <div class="iris">
        <div class="pupil"></div>
      </div>
    </div>
  </div>
  <div class="spotlight"></div>
  <div class="scan-line"></div>
  <div class="glitch-text">Always Watching</div>
  <div class="footer-text">Obey. Trust. Consume</div>
</div>
<style>
.card {
  background-color: #222;
  border: 10px solid rgb(161, 156, 116);
  padding: 30px;
  width: 400px;
  text-align: center;
  position: relative;
  box-shadow: 9px 11px 1px rgb(0, 0, 0);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  overflow: hidden;
  z-index: 1;
}
.card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: repeating-linear-gradient(
    0deg,
    rgba(255, 255, 255, 0.05),
    rgba(255, 255, 255, 0.05) 1px,
    transparent 1px,
    transparent 2px
  );
  opacity: 0.3;
  pointer-events: none;
  z-index: 2;
  animation: tv-static 0.2s infinite linear alternate;
}
.eye {
  width: 90px;
  height: 50px;
  background: radial-gradient(circle at 30% 30%, #fff, #e6e6e6);
  border-radius: 50%;
  position: absolute;
  top: 90px;
  left: 65px;
  overflow: hidden;
  box-shadow: 0 0 0 10px rgb(115, 112, 92), 15px 15px 0 #000,
    inset -5px -5px 10px rgba(0, 0, 0, 0.2),
    inset 5px 5px 10px rgba(255, 255, 255, 0.3);
  z-index: 2;
  animation: blink 6s infinite cubic-bezier(0.76, 0, 0.24, 1);
}
.pupil {
  width: 16px;
  height: 16px;
  background: rgb(207, 19, 19);
  border-radius: 50%;
  background: radial-gradient(circle at 50% 50%, #000, #444);
  border: 2px solid #fff;
  position: absolute;
  top: 14px;
  left: 14px;
  box-shadow: inset 0 0 10px rgba(203, 4, 4, 0.2), 0 0 10px rgba(0, 0, 0, 0.5);
}
.iris {
  width: 45px;
  height: 45px;
  background: #000;
  border-radius: 50%;
  position: absolute;
  top: 2px;
  left: 22px;
  animation: look-around 6s infinite;
  animation-timing-function: ease-in-out;
}
.title {
  color: rgb(255, 255, 255);
  margin-top: 30px;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-size: 28px;
  padding-bottom: 33px;
  text-shadow: 3px 3px #000;
  z-index: 3;
  position: relative;
  display: inline-block;
}
.glitch-text {
  color: #fff;
  font-size: 20px;
  margin-top: 20px;
  position: relative;
  display: inline-block;
  text-shadow: 2px 2px #000;
  z-index: 3;
}
.scan-line {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 6px;
  background: rgba(75, 68, 68, 0.5);
  animation: scan 2.5s linear infinite;
  z-index: 4;
}
</style>

<!-- Filename -->
0xnihilism_cold-tiger-22.html
```

#### OUTPUT:
```json
{
  "description": "A dark-themed card featuring the Eye of Providence symbol with animated blinking eye, glitch text effects, scan line animation, and TV static overlay, creating a dystopian surveillance aesthetic with beige border and black shadow.",
  "production_filename": "eyeOfProvidenceCard",
  "colors": ["#222222", "#a19c74", "#c6b571", "#73705c", "#000000", "#ffffff", "#cf1313", "#444444"],
  "tags": ["card", "dark", "animation", "3d", "hover effect", "advanced", "black", "glitch"]
}
```

---

#### INPUT:
```html
<input class="neo-input" placeholder="Enter text" />
<style>
  .neo-input {
    background: #ecf0f3;
    box-shadow: inset 3px 3px 6px #d1d9e6, inset -3px -3px 6px #ffffff;
    border-radius: 12px;
    color: #333;
  }
</style>

<!-- Filename -->
0x3ther_afraid-eagle-38.html
```

#### OUTPUT:
```json
{
  "description": "A neumorphic input field with soft inset shadows creating a subtle 3D effect, featuring light gray background with darker inner shadows and lighter outer highlights for a tactile appearance.",
  "production_filename": "neumorphicInputField",
  "colors": ["#ecf0f3", "#d1d9e6", "#ffffff", "#333333"],
  "tags": ["input", "neumorphism", "3d", "minimal", "rounded", "modern"]
}
```

---

#### INPUT:
```html
<label class="switch">
  <input type="checkbox">
  <span class="slider round"></span>
</label>
<style>
  .switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
  }
  .slider {
    background-color: #ccc;
  }
  input:checked + .slider {
    background-color: #2196f3;
  }
</style>

<!-- Filename -->
0xnihilism_fast-cat-82.html
```

#### OUTPUT:
```json
{
  "description": "A custom toggle switch with rounded edges that transitions from gray to blue when activated, featuring a sliding animation and clean minimal design for easy state indication.",
  "production_filename": "roundedToggleSwitch",
  "colors": ["#cccccc", "#2196f3"],
  "tags": ["switch", "rounded", "animation", "blue", "minimal", "hover"]
}
```

---

#### INPUT:
```html
<div class="loader"></div>
<style>
.loader {
  border: 8px solid #f3f3f3;
  border-top: 8px solid #555;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  animation: spin 1s linear infinite;
}
</style>

<!-- Filename -->
0x3ther_heavy-dragon-56.html
```

#### OUTPUT:
```json
{
  "description": "A circular spinning loader with a dual-tone border creating a clean, minimal loading indicator that rotates continuously to provide visual feedback during loading states.",
  "production_filename": "circularSpinnerLoader",
  "colors": ["#f3f3f3", "#555555"],
  "tags": ["loader", "animation", "circle", "minimal", "centered"]
}
```

---

#### INPUT:
```html
<div class="tooltip">Hover over me<span class="tooltiptext">Tooltip text</span></div>
<style>
.tooltiptext {
  background-color: #000;
  color: #fff;
}
</style>

<!-- Filename -->
0xnihilism_helpless-rattlesnake-54.html
```

#### OUTPUT:
```json
{
  "description": "A tooltip component that reveals information on hover using a high-contrast black background with white text, providing contextual information without cluttering the interface.",
  "production_filename": "hoverTooltipBlackWhite",
  "colors": ["#000000", "#ffffff"],
  "tags": ["tooltip", "hover", "black", "white", "minimal", "text"]
}
```

---

#### INPUT:
```html
<button class="glitch-btn">HACK</button>
<style>
.glitch-btn {
  color: #00ff00;
  text-shadow: 1px 0 red, -1px 0 blue;
}
</style>

<!-- Filename -->
0xnihilism_pretty-fireant-33.html
```

#### OUTPUT:
```json
{
  "description": "A glitch-style button with RGB split text effect and green digital font, creating a cyberpunk aesthetic with color channel separation for a distorted, technological appearance.",
  "production_filename": "glitchButtonRGB",
  "colors": ["#00ff00", "#ff0000", "#0000ff"],
  "tags": ["button", "glitch", "animation", "text", "modern", "bold"]
}
```

---

#### INPUT:
```html
<div class="card">
  <h3>John Doe</h3>
</div>
<style>
.card {
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 1rem;
}
</style>

<!-- Filename -->
0xnihilism_quiet-dog-6.html
```

#### OUTPUT:
```json
{
  "description": "A minimalist profile card with a clean white background and subtle light gray border, featuring simple typography and ample padding for a clean, uncluttered presentation of information.",
  "production_filename": "simpleProfileCard",
  "colors": ["#ffffff", "#cccccc"],
  "tags": ["card", "minimal", "white", "simple", "centered"]
}
```

---

#### INPUT:
```html
<button style="background-color: #000; color: #fff;">Dark Theme</button>
```

#### OUTPUT:
```json
{
  "description": "A simple dark-themed button with white text on black background, providing high contrast for clear visibility and a modern, sleek appearance with minimal styling.",
  "production_filename": "darkThemeButton",
  "colors": ["#000000", "#ffffff"],
  "tags": ["button", "dark", "minimal", "simple", "text"]
}
```

---

#### INPUT:
```html
<input type="radio" name="theme" value="dark"> Dark
<input type="radio" name="theme" value="light"> Light
<style>
input[type="radio"] {
  accent-color: #ff9900;
}
</style>
```

#### OUTPUT:
```json
{
  "description": "Styled radio buttons with orange accent color for selection, providing clear visual feedback for the selected option while maintaining a clean, minimal interface design.",
  "production_filename": "orangeAccentRadioButtons",
  "colors": ["#ff9900"],
  "tags": ["radio", "minimal", "orange", "input", "simple"]
}
```
