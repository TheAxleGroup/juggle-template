module.exports = {
    mode: process.env.NODE_ENV ? 'jit' : undefined,
    purge: {
        content: [
            './app/**/templates/**/*.html',
            '/app/**/templates/**/*.html',
            './app/**/static/js/*.js',
            './app/**/page/blocks/*.py',
        ],
        safelist: [
            'col-span-1',
            'col-span-2',
            'col-span-3',
            'col-span-4',
            'col-span-5',
            'col-span-6',
            'col-span-7',
            'col-span-8',
            'col-span-9',
            'col-span-10',
            'col-span-11',
            'col-span-12',
            'gap-x-2',
            'gap-x-4',
            'gap-x-8',
            'gap-x-12',
            'item-2',
            'item-3',
            'item-4',
            'bg-gray-light',
            'bg-gray-lightest',
            'bg-red',
            'bg-yellow',
            'bg-green',
            'bg-azure',
            'border-red',
            'border-yellow',
            'border-green',
            'border-azure',
            'bg-secondary-dark',
        ]
    },
    darkMode: false, // or 'media' or 'class'
    theme: {
        screens: {
            sm: '576px',
            md: '768px',
            lg: '992px',
            xl: '1300px',
        },
        colors: {
            transparent: 'transparent',
            current: 'currentColor',
            primary: {
                DEFAULT: '#00164E',
                dark: '#00164E',
                darker: '#00164E'
            },
            secondary: {
                DEFAULT: '#488AC9',
                dark: '#425ABA',
            },
            navy: {
                DEFAULT: '#00164E',
                mid: '#10266a',
                light: '#273C91',
            },
            gray: {
                DEFAULT: '#333',
                brand: '#323E48',
                lightest: '#F7F8F8',
            },
            body: {
                DEFAULT: '#e9eaed',
            },
            nav: {
                DEFAULT: '#080d19'
            },
            anchor: {
                DEFAULT: '#00164E',
                hover: '#888888',
            },
            button: {
                DEFAULT: '#00164E',
                hover: '#323e48',
                white: '#fff'
            },
            white: {
                DEFAULT: '#FFFFFF',
            },
            black: {
                DEFAULT: '#000',
            },
            blue: {
                DEFAULT: '#e2e2eb',
            },
            orange: {
                DEFAULT: '#f15c3b',
            },
            red: {
                DEFAULT: '#F15D3C',
            },
            green: {
                DEFAULT: '#84CBA2',
            },
            yellow: {
                DEFAULT: '#FDB61B',
            },
            azure: {
                DEFAULT: '#478AC9',
            },
        },
        fontFamily: {
            header: ['Poppins', 'sans-serif'],
            body: ['Poppins', 'sans-serif'],
        },
        borderRadius: {
            'none': '0',
            sm: '5px',
            DEFAULT: '10px',
            'full': '9999px',
        },
        borderWidth: {
            DEFAULT: '1px',
            '0': '0',
            '2': '2px',
            '3': '3px',
            '4': '4px',
            '6': '6px',
            '8': '8px',
        },
        fontSize: {
            '12': '.75rem',
            '14': '.875rem',
            '15': '.9375rem',
            base: '1rem',
            '18': '1.125rem',
            '20': '1.25rem',
            '22': '1.375rem',
            '24': '1.5rem',
            '26': '1.625rem',
            '28': '1.75rem',
            '32': '2rem',
            '36': '2.25rem',
            '40': '2.5rem',
            '42': '2.625rem',
            '48': '3rem',
            '50': '3.125rem',
            '54': '3.375rem',
            '64': '4rem',
            '80': '5rem',
            '90': '5.625rem',

        },
        extend: {
            minHeight: (theme) => theme('spacing'),
            lineHeight: {
                'looser': '2.25',
            },
            fill: {
                'transparent': 'transparent',
            },
            spacing: {
                'unset': 'unset',
            }
        },
        variants: {
            extend: {
                scale: ['group-hover'],
            }
        },
        boxShadow: {
            'plan': '0px 0px 12px 3px rgba(0, 0, 0, 0.10);',
        }
    },
    plugins: [
        require('@tailwindcss/forms'),
    ],
}
