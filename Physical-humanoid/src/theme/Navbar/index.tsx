import React from 'react';
import Navbar from '@theme-original/Navbar';
import type { Props } from '@docusaurus/theme-classic/lib/theme/Navbar';

export default function NavbarWrapper(props: Props): JSX.Element {
  return (
    <Navbar {...props} />
  );
}