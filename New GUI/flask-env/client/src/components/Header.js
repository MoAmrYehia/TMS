import React from "react";
import Navbar from "react-bootstrap/Navbar";
import logo from "./logo_b.png";
// import {Navbar, NavbarBrand, Container} from 'reactstrap';

function Header() {
  return (
    <>
      <Navbar bg="dark" variant="dark">
        <Navbar.Brand href="/">
          <img
            alt=""
            src={logo}
            width="30"
            height="30"
            className="d-inline-block align-top"
          />{" "}
          SkillRoad
        </Navbar.Brand>
      </Navbar>
    </>
    // <>
    //     <header className="header-global">
    //       <Navbar
    //         className="navbar-main navbar-transparent navbar-light"
    //         expand="lg"
    //         id="navbar-main"
    //       >
    //         <Container>
    //           <NavbarBrand className="mr-lg-5" to="/home" tag={Link}>
    //             <img
    //               alt="SkillRoad"
    //               height="30"
    //               width="30"
    //               src={logo}
    //             />
    //           </NavbarBrand>
    //           <button className="navbar-toggler" id="navbar_global">
    //             <span className="navbar-toggler-icon" />
    //           </button>
    //         </Container>
    //       </Navbar>
    //     </header>
    //   </>
  );
}

export default Header;
