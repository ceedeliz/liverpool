import React, { useState, useEffect } from "react";
import axios from "axios";
import { useHistory, Link } from "react-router-dom";
import Button from "@material-ui/core/Button";
const Home = () => {
  const history = useHistory();
  const [users, setUser] = useState([]);

  useEffect(() => {
    loadUsers();
  }, []);


  const loadUsers = async () => {
    const result = await axios.get(
      `http://localhost:8000/empleados`, {
        headers: {
          "Access-Control-Allow-Origin": "*"
         }
        }
    );
    setUser(result.data);
  };
  return (
    <div className="home-page">
      <table className="table">
        <thead className="thead-dark">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Empleado</th>
            <th scope="col">Sociedad</th>
            <th scope="col">Ubicacion</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user, index) => (
            <tr key={user.id}>
              <th scope="row">{index + 1}</th>
              <td>{user.nombre}</td>
              <td>{user.sociedad}</td>
              <td>{user.ubicacion}</td>
              <td>
              <Button
                variant="contained"
                onClick={() => history.push(`/user/${user.id}`)}
              >
                View
              </Button>
              {/* <Link class="btn btn-outline-primary mr-2" to={`./edituser/${user.id}`}>Edit</Link> */}
              <Button
                variant="contained"
                color="primary"
                onClick={() => history.push(`/edituser/${user.id}`)}
              >
                Edit
              </Button>
              <Button
                variant="contained"
                color="secondary"
                onClick={() => deleteUser(user.id)}
              >
                Delete
              </Button></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Home;
