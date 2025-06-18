/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
  animation: {
    'pulse-slow': 'pulse 6s ease-in-out infinite',
  },
  boxShadow: {
        'custom-glow': '0 4px 30px rgba(0, 255, 163, 0.5)',
        'custom-deep': '0px 10px 25px rgba(0, 0, 0, 0.4)',
        'custom-outline': '0 0 0 3px rgba(66, 153, 225, 0.5)',
        'green-shadow': '2px 2px 0px 3px rgba(0,0,0,0.8)'
      },
}
  },
  plugins: [],
}