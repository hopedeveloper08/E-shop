import React from "react";
import { Container, Row, Col, Badge } from "react-bootstrap";

function Footer() {
  return (
    <footer>
      <Container>
        <Row>
          <Col className="text-center footer-font-size py-3">
            Copyright &copy; E-Shop
            <br />
            Developed by{" "}
            <a target="blank" href="https://github.com/hopedeveloper08">
              <Badge>
                <p className="d-inline align-middl fw-lighter">
                  hopedeveloper08<i class="fab fa-github ms-2"></i>
                </p>
              </Badge>
            </a>
          </Col>
        </Row>
      </Container>
    </footer>
  );
}

export default Footer;
