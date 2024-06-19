const colors = require('tailwindcss/colors')


module.exports = {
    purge: {},
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                'cyan': colors.cyan,
                'light-blue': colors.lightBlue,
                'lime': colors.lime,
                'true-gray': colors.trueGray,
                'warm-gray': colors.warmGray,
            },
        },
    },
    variants: {
        extend: {
            backgroundColor: ['active', 'checked'],
            borderColor: ['checked'],
        },
    },
    plugins: [
        require("@tailwindcss/forms"),
    ],
}


// module.exports = {
//     darkMode: false,
//     future: {
//         removeDeprecatedGapUtilities: true,
//         purgeLayersByDefault: true,
//     },
//     purge: {
//         enabled: false, //true for production build
//         content: [
//                 '../**/templates/*.html',
//                 '../**/templates/**/*.html'
//         ]
//     },
//     theme: {
//         colors: {
//             'cyan': colors.cyan,
//             'light-blue': colors.lightBlue,
//             'lime': colors.lime,
//             'true-gray': colors.trueGray,
//             'warm-gray': colors.warmGray,
//         },
//         extend: {},
//     },
//     variants: {
//         extend: {
//             backgroundColor: ['active'],
//         },
//     },
//     plugins: [],
// }
