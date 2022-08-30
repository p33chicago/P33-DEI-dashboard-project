/** @type {import('tailwindcss').Config} */ 
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    screens: {
      'xs': '320px',
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
    colors: {
      'black': '#04352d',
      'white': '#f4f4f4',
      'dark-gray': '#e0e5ec',
      'medium-gray': '#88b6b6',
      'light-gray': '#d9d9d9',
      'really-light-gray': '#e0e5ec',
      'brand-primary-dark-green': '#00715e',
      'brand-primary-green': '#0db296',
      'brand-primary-light-green': '#56cbb8',
      'brand-primary-really-light-green': '#dee9e8',
      'blue': '#1d59b8',
      'fail-red': '#981717',
      'warn-orange': '#ff7213',
      'heads-up-yellow': '#ffa913',
    },
    fontFamily: {
      mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'Liberation Mono', 'Courier New', 'monospace'],
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    
    },
    fontWeight: {
      'default-regular': 400,
      'default-bold': 600
    },
    extend: {}
  },
  plugins: []
};
