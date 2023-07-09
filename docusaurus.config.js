// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');
const math = require('remark-math');
const katex = require('rehype-katex');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Recohut Data Bootcamp',
  tagline: 'Embrace excellence, embrace changes, embrace data',
  url: 'https://www.recohut.in/',
  baseUrl: '/',
  onBrokenLinks: 'ignore',
  onBrokenMarkdownLinks: 'ignore',
  trailingSlash: false,
  favicon: '/img/branding/favicon-black.svg',
  organizationName: 'sparsh-ai',
  projectName: 'recohut',
  themes: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      {
        hashed: true,
      },
    ],
    '@saucelabs/theme-github-codeblock',
    '@docusaurus/theme-mermaid',
  ],
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  markdown: {
    mermaid: true,
  },
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          showLastUpdateAuthor: true,
          showLastUpdateTime: true,
          // path: 'docs',
          // routeBasePath: 'docs',
          remarkPlugins: [math],
          rehypePlugins: [katex],
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
        gtag: {
          trackingID: 'G-B4S1B1ZDTT',
          anonymizeIP: false,
        },
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
          ignorePatterns: ['/tags/**'],
          filename: 'sitemap.xml',
        },
        // blog: {
        //   path: 'labs',
        //   blogTitle: 'Labs',
        //   blogDescription: 'Data Engineering Industrial Hands On Labs',
        //   blogSidebarCount: 'ALL',
        //   blogSidebarTitle: 'Recent labs',
        //   routeBasePath: 'labs',
        //   postsPerPage: 10,
        //   showReadingTime: false,
        // },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // announcementBar: {
      //   id: 'support_us',
      //   content:
      //     '⭐️ <b>If you like Recohut, give it a star on <a target="_blank" rel="noopener noreferrer" href="https://github.com/datalaker/recohut-data-bootcamp">GitHub</a>, Appreciate our efforts by donating <a target="_blank" rel="noopener noreferrer" href="https://www.buymeacoffee.com/recohut">here ☕</a></b>',
      //   backgroundColor: '#fafbfc',
      //   textColor: '#091E42',
      //   isCloseable: true,
      // },
      navbar: {
        title: 'Bootcamp',
        logo: {
          alt: 'Recohut Logo',
          src: '/img/branding/favicon-color.svg',
        },
        items: [
          {
            label: "Docs",
            position: "left",
            to: "docs/introduction"
          },
          // {
          //   to: 'blog',
          //   position: 'left',
          //   label: 'Blog',
          // },
          {
            href: 'https://github.com/sparsh-ai/recohut',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      docs: {
        sidebar: {
          autoCollapseCategories: true,
          hideable: true,
        },
      },
      footer: {
        style: 'dark',
        links: [
        ],
        // logo: {
        //   alt: 'Recohut Logo',
        //   src: '/img/branding/logo-no-background-small.png',
        //   href: 'https://www.recohut.in/',
        // },
        copyright: `Copyright © ${new Date().getFullYear()} Bootcamp. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
      metadata: [{ name: 'keywords', content: 'data science, data engineering, data analytics' }],
    }),
};

module.exports = config;
