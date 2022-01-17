class MyComponent extends StreamlitComponentBase {
    public render(): ReactNode {
        // Access arguments from Python via `this.props.args`:
        const greeting = this.props.args["greeting"]
        const name = this.props.args["name"]
        return <div>{greeting}, {name}!</div>
    }
}
