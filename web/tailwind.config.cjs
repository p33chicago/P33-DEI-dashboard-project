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
    borderColor: {
      DEFAULT: 'var(--brand-primary-dark-green)'
    },
    extend: {
      colors: {
        'black': 'var(--black)',
        'white': 'var(--white)',
        'dark-gray': 'var(--dark-gray)',
        'medium-gray': 'var(--medium-gray)',
        'light-gray': 'var(--light-gray)',
        'really-light-gray': 'var(--really-light-gray)',
        'brand-primary-dark-green': 'var(--brand-primary-dark-green)',
        'brand-primary-green': 'var(--brand-primary-green)',
        'brand-primary-light-green': 'var(--brand-primary-light-green)',
        'brand-primary-really-light-green': 'var(--brand-primary-really-light-green)',
        'blue': 'var(--blue)',
        'fail-red': 'var(--fail-red)',
        'warn-orange': 'var(--warn-orange)',
        'heads-up-yellow': 'var(--heads-up-yellow)',
      }
    }
  },
  plugins: []
};
