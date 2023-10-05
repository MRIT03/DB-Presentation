/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: ["./templates/**/*.{html,htm}"],
  theme: {
    extend: {},
    fontFamily: {
      poppins: ['Poppins']
    }
  },

  plugins: [
    require('@tailwindcss/forms'),
  ],
}


