import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import LandingPage from "./components/LandingPage";
import Footer from "./components/Footer";
import ProfilePage from "./components/ProfilePage/ProfilePage";
import FileSubmission from "./components/FileSubmission";
import Header from "./components/Header";

import "bootstrap/dist/css/bootstrap.min.css";

// import "./assets/css/argon-design-system-react.min.css";
// import "./assets/css/argon-design-system-react.css.map";

class App extends Component {
  render() {
    return (
      <Router>
        <div className="#9CF6F6">
          <Header />
          <Switch>
            <Route exact path="/" component={LandingPage} />
            <Route exact path="/submit" component={FileSubmission} />
            <Route exact path="/profile" component={ProfilePage} />
            <Route exact path="/footer" component={Footer} />
          </Switch>
          <Footer />
        </div>
      </Router>
    );
  }
}

export default App;
