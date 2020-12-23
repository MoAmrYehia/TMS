import React, { Fragment } from "react";
import Home from "./Home";
import Button from "react-bootstrap/Button";
import { Link } from "react-router-dom";
function LandingPage() {
  return (
    <Fragment>
      <Home />
      <div className="container">
        <div className="text-center">
          <p>
            SkillRoad is a career advisor platform that allows our users to be
            ready for their next career level. <br />
            It is your guide to finding the appropriate career path for you.
          </p>
        </div>
        <div className="text-center">
          {/* <Link to={"/profile"}>
          <Button variant="dark">Start your SkillRoad</Button>
        </Link> */}
          <Link to={"/submit"}>
            <Button variant="dark">Get Started!</Button>
          </Link>
        </div>
      </div>
    </Fragment>
  );
}
export default LandingPage;
