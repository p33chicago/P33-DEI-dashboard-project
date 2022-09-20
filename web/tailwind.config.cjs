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
      'fullnav': '815px',
    },
    fontFamily: {
      mono: ['Roboto Mono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'Liberation Mono', 'Courier New', 'monospace'],
      sans: ['Roboto', 'sans-serif'],
      'sans-alternate': ['Fjalla One', 'sans-serif']
    },
    fontWeight: {
      'regular': 100,
      'bold': 600
    },
    dropShadow: {
      'card': '0 4px 4px rgb(0 0 0 / 0.25)'
    },
    borderColor: {
      DEFAULT: 'var(--brand-primary-dark-green)'
    },
    extend: {
      colors: {
        'black': '#04352d',
        'white': '#f4f4f4',
        'dark-gray': '#787A7D',
        'medium-gray': '#B8B6B6',
        'light-gray': '#d9d9d9',
        'really-light-gray': '#e0e5ec',
        'brand-primary-green': '#0db296',
        'brand-primary-dark-green': '#00715e',
        'brand-primary-dark-green-banner-background': '#00483e',
        'brand-primary-light-green': '#56cbb8',
        'brand-primary-really-light-green': '#dee9e8',
        'blue': '#1d59b8',
        'fail-red': '#981717',
        'warn-orange': '#ff7213',
        'heads-up-yellow': '#ffa913'
      },
      backgroundImage: {
        'chicago': "url('/chicago.svg')",
      }
    }
  },
  plugins: []
};
