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
      'fullnav': '810px',
    },
    colors: {
      'black': '#04352d',
      'white': '#f4f4f4',
      'dark-gray': '#e0e5ec',
      'medium-gray': '#88b6b6',
      'light-gray': '#d9d9d9',
      'really-light-gray': '#e0e5ec',
      'brand-primary-dark-green': 'var(--brand-primary-dark-green)',
      'brand-primary-green': 'var(--brand-primary-green)',
      'brand-primary-light-green': '#56cbb8',
      'brand-primary-really-light-green': 'var(--brand-primary-really-light-green)',
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
      'regular': 100,
      'bold': 600
    },
    dropShadow: {
      'card': '0 4px 4px rgb(0 0 0 / 0.25)'
    },
    extend: {}
  },
  plugins: []
};
