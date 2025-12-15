require('dotenv').config();

import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'A Textbook by Syed Ali Raza',
  favicon: 'img/favicon.ico',
  future: {
    v4: true,
  },
  url: 'https://Syed-AliRaza005.github.io',
  baseUrl: '/',
  organizationName: 'Syed-AliRaza005',
  projectName: 'AI-robotics',
  trailingSlash: false,
  deploymentBranch: 'gh-pages',
  onBrokenLinks: 'throw',
    customFields: {
    back_end_url: process.env.back_end_url,
  },
  i18n: {
      defaultLocale: 'en',
      locales: ['en'],
    },
  
    presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl:
            'https://github.com/Syed-AliRaza005/AI-robotics'
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Physical AI & Humanoid Robotics',
      logo: {
        alt: 'Syed Ali Raza Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          to: '/docs/overview',
          label: 'Overview',
          position: 'left',
        },
        {
          href: 'https://github.com/Syed-AliRaza005/AI-robotics',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Textbook',
          items: [
            {
              label: 'Overview',
              to: '/docs/overview',
            },
            {
              label: 'Learning Outcomes',
              to: '/docs/learning-outcomes',
            },
            {
              label: 'Hardware Requirements',
              to: '/docs/hardware-requirements',
            },
            {
              label: 'Assessments',
              to: '/docs/assessments/introduction',
            },
          ],
        },
        {
          title: 'Connect with Me ',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/Syed-AliRaza005/AI-robotics',
            },
            {
              label: 'Linkedin',
              href: 'https://www.linkedin.com/in/syed-ali-raza-hassan-6166a02ba/',
            },
            {
              label: 'Portfolio',
              href: 'https://portfolio-sarh.vercel.app/',
            },
            {
              label: 'Instagram',
              href: 'https://www.instagram.com/_itz_ali_005/',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Syed Ali Raza. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['python'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;