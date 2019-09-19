module.exports = {
  // options...
  devServer: {
    hot: true,
    hotOnly: true,
    disableHostCheck: true,
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
      "Access-Control-Allow-Headers":
        "X-Requested-With, content-type, Authorization"
    },
    watchOptions: {
      poll: 1000,
      ignored: "/app/node_modules/"
    }
  }
};
