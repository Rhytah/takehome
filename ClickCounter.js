class App extends Component {
    constructor(props) {
      super(props);
      this.state = { value: 0 };
      this.handlebuttonClick = this.handlebuttonClick.bind(this);
    }
  
    handlebuttonClick(event) {
      this.setState({ value: this.state.value + 1 });
    }
  
    render() {
      return (
        <div>
          <button onClick={this.handlebuttonClick}>
            Click count: {this.state.value}
          </button>
        </div>
      );
    }
  }
  
  export default App;
  