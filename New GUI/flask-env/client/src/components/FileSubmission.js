import React, { Component } from "react";
import { Link } from "react-router-dom";

import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";

class FileSubmission extends Component {
  //   constructor(props) {
  //     super(props);

  //     this.state = {
  //       file: "",
  //     };

  //     this.handleUpload = this.handleUpload.bind(this);
  //   }

  //   handleUpload(e) {
  //     e.preventDefault();

  //     const data = new FormData();
  //     data.append("file", this.uploadInput.files[0]);
  //     data.append("filename", this.fileName.value);

  //     fetch("/api/upload/", {
  //       method: "POST",
  //       body: data,
  //     }).then((response) => {
  //       //   response.json().then((body) => {
  //       //     this.setState({ file: `http:///${body.file}` });
  //       //   });
  //       console.log(response.json());
  //     });
  //   }
  constructor(props) {
    super(props);
    this.state = {
      selectedFile: null,
      disabled: true,
      submitted: false,
      parsedCvData: {
        name: null,
        mobil_number: null,
        email: null,
        degree: [],
        skills: [],
      },
    };
  }

  onChangeHandler = (e) => {
    this.setState({
      selectedFile: e.target.files[0],
      disabled: false,
    });
  };

  onClickHandler = () => {
    const data = new FormData();
    data.append("file", this.state.selectedFile);

    fetch("/api/upload/", {
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
          submitted: true,
          parsedCvData: data.parsed_cv,
        });
        console.log(this.state.parsedCvData);
        console.log(this.state.submitted);
      });
  };

  render() {
    // console.log("Rendering", this.state);
    // const { info } = this.state;
    // console.log("info", info);
    // const email =
    //   info && info.parsed_cv ? "Email: " + info.parsed_cv.email : "";
    // const skills = info && info.parsed_cv ? info.parsed_cv.skills : [];

    const { disabled, submitted, parsedCvData } = this.state;

    const cvData = (
      <Container className="mb-5">
        <Row
          className="justify-content-md-left mb-5"
          style={{ marginTop: 150, marginLeft: 200 }}
        >
          <Col
            className="mb-5"
            md="auto"
            style={{ marginTop: 50, marginRight: 100 }}
          >
            <div className="text-center mb-3">
              <h3>Name</h3>
              <div className="h6 font-weight-300">{parsedCvData.name}</div>
              <hr />
            </div>
            <div className="text-center  mb-3">
              <h3>Phone number</h3>

              <div className="h6 font-weight-300">
                {parsedCvData.mobile_number}
              </div>
              <hr />
            </div>
            <div className="text-center  mb-3">
              <h3>Email</h3>

              <div className="h6 font-weight-300">{parsedCvData.email}</div>
              <hr />
            </div>
          </Col>
          <Col className="mb-5" md="auto">
            <div className="text-center  mb-3">
              <h3>Degree</h3>

              <div className="h6 font-weight-300">
                {parsedCvData.degree.map((d) => (
                  <h6>{d}</h6>
                ))}
              </div>
              <hr />
            </div>
            <div className="text-center  mb-3">
              <h3>Skills</h3>

              <div className="h6 font-weight-300">
                {parsedCvData.skills.map((skill) => (
                  <h6>{skill}</h6>
                ))}
              </div>
              <hr />
            </div>
            <div className="mt-3">
              <Link to={"/profile"}>
                <Button size="sm" variant="danger" href="/profile">
                  Discover your SkillRoad!
                </Button>
              </Link>
            </div>
          </Col>
        </Row>
      </Container>
    );

    const empty = (
      <div>
        <Container className="mb-5">
          <Row
            className="justify-content-md-center mb-5"
            style={{ marginTop: 245, marginLeft: 200 }}
          >
            <Col className="mb-5" md="auto">
              <div className="text-center mt-5 mb-3">
                <p>Upload your CV to see your profile...</p>
              </div>
            </Col>
          </Row>
        </Container>
      </div>
    );

    return (
      //   <form onSubmit={this.handleUpload}>
      //     <div>
      //       <input
      //         ref={(ref) => {
      //           this.uploadInput = ref;
      //         }}
      //         type="file"
      //       />
      //     </div>
      //     {/* <div>
      //       <input
      //         ref={(ref) => {
      //           this.fileName = ref;
      //         }}
      //         type="text"
      //         placeholder="Enter the desired name of file"
      //       />
      //     </div> */}
      //     <br />
      //     <div>
      //       <button>Upload</button>
      //     </div>
      //     {/* <img src={this.state.imageURL} alt="img" /> */}
      //   </form>
      <Container>
        <Row>
          <Col className="col-2">
            <Row className="" style={{ marginTop: 250 }}>
              <Col md="auto">
                <input
                  type="file"
                  name="file"
                  onChange={this.onChangeHandler}
                />
              </Col>
            </Row>

            <Row className="" style={{ marginTop: 50 }}>
              <Col md="auto">
                <Button
                  size="lg"
                  variant="dark"
                  disabled={disabled}
                  onClick={this.onClickHandler}
                >
                  Upload
                </Button>
              </Col>
            </Row>
          </Col>
          <Col>{submitted ? cvData : empty}</Col>
        </Row>

        {/* <Row className="justify-content-md-center" style={{ marginTop: 30 }}>
          <Col md="auto">
            <p>{email}</p>
          </Col>
        </Row>

        <Row
          className="justify-content-md-center"
          style={{ marginTop: 30, marginBottom: 30 }}
        >
          <Col md="auto">
            <ul>
              {skills.map((skill) => (
                <li key={skill}>
                  <p>{skill}</p>
                </li>
              ))}
            </ul>
          </Col>
        </Row> */}
      </Container>
    );
  }
}

export default FileSubmission;
