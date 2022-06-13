import React from 'react';
import axios from 'axios';

class App extends React.Component {

  state = {
    details: [],
  }

  componentDidMount() {

    let data;

    axios.get('http://127.0.0.1:8000/api/InventoryAPI/')
      .then(res => {
        data = res.data;
        this.setState({
          details: data
        });
      })
      .catch(err => { })
  }

  render() {
    return (
      <table class="table" id="book-table">

        <thead>
          <tr>
          <th>name</th>
        <th>quantity</th>
        <th>Date Created</th>
        <th>Date Updated</th>
        <th>Action</th>

          </tr>
        </thead>
        <tbody>
        {this.state.details.map((detail, id) => (
          <tr>
          <td>{detail.name}</td>
            <td>{detail.quantity}</td>
            <td>{detail.date_created}</td>
            <td>{detail.date_updated}</td>
            <td><a href='' class="btn btn-warning">Update</a></td>                                       
              <td><a href='' class="btn btn-danger" onclick="return confirm('Are you sure you want to delete this?');">Delete</a></td>  
          </tr>
)

)}  

        </tbody>
      </table>
    );
  }
}

export default App;
