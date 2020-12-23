import React, { Component } from "react";

import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";

class ProfilePage extends Component {
  constructor() {
    super();
    this.state = {
      skill: null,
      skills: [],
    };
    this.onSubmit = this.onSubmit.bind(this);
  }

  onChangeHandler = (e) => {
    e.preventDefault();
    this.setState({
      skill: e.target.value,
    });
  };

  onSubmit = (e) => {
    e.preventDefault();
    const data = new FormData();
    data.append("skill", this.state.skill);

    console.log(data);

    fetch("/api/predict/skills", {
      method: "POST",
      body: data,
    })
      .then((res) => {
        // console.log();
        const ret = res.json();
        // console.log(ret);
        return ret;
      })
      .then((data) => {
        this.setState({
          skills: data,
        });
      });
  };

  render() {
    const { skills } = this.state;
    return (
      <Container>
        <Row className="justify-content-center mb-5" style={{ marginTop: 250 }}>
          <Col className="col-3 mb-4">
            <form onSubmit={this.onSubmit}>
              <div className="form-row">
                <div className="form-group">
                  <div className="form-group">
                    <label for="inputState">
                      Select one skill you own and see what you can learn next!
                    </label>
                    <select
                      className="form-control"
                      onChange={this.onChangeHandler}
                    >
                      <option selected>Choose...</option>
                      <option>Bash</option>
                      <option>C</option>
                      <option>C++</option>
                      <option>C#</option>
                      <option>COBOL</option>
                      <option>CSS</option>
                      <option>Java</option>
                      <option>JavaScript</option>
                      <option>Objective-C</option>
                      <option>PHP</option>
                      <option>Python</option>
                      <option>R</option>
                      <option>Scala</option>
                      <option>SQL</option>
                    </select>
                  </div>
                  <div>
                    <Button type="submit" size="sm" variant="danger">
                      Find out more!
                    </Button>
                  </div>
                </div>
              </div>
            </form>
          </Col>

          <Col className="mb-5" style={{ marginTop: -50, marginLeft: 250 }}>
            <h2>What you can learn next?</h2>
            <hr />
            <div className="">
              <div className="h6 font-weight-300">
                {skills.map((skill) => (
                  <h6>{skill[0]}</h6>
                ))}
              </div>
              <hr />
            </div>
          </Col>
        </Row>
      </Container>
    );
  }
}

export default ProfilePage;
