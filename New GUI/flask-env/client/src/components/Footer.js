import React, { Component } from "react";

import Navbar from "react-bootstrap/Navbar";
import logo from "./octo.png";

export class Footer extends Component {
  render() {
    return (
      <>
        <Navbar
          fixed="bottom"
          bg="dark"
          variant="dark"
          classname="navbar-right"
        >
          <Navbar.Brand
            classname="ml-auto"
            href="https://github.com/MoAmrYehia/HackTheNortheast"
          >
            <img
              alt=""
              src={logo}
              width="30"
              height="30"
              className="d-inline-block align-top"
            />
          </Navbar.Brand>
        </Navbar>
      </>
    );
  }
}

export default Footer;

// import React from 'react';
// import Navbar from 'react-bootstrap/Navbar';
// import logo from './octo.png';

// function Footer() {
//     return (
//         <>
//             <Navbar fixed="bottom" bg="dark" variant="dark" classname="navbar-right">
//                 <Navbar.Brand classname="ml-auto" href="https://github.com/MoAmrYehia/HackTheNortheast">
//                     <img
//                         alt=""
//                         src={logo}
//                         width="30"
//                         height="30"
//                         className="d-inline-block align-top"
//                     />
//                 </Navbar.Brand>
//             </Navbar>
//         </>
//     )
// }

// export default Footer
