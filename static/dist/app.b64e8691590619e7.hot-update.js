"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(typeof self !== 'undefined' ? self : this)["webpackHotUpdatevue_ticketswap"]("app",{

/***/ "./src/router.js":
/*!***********************!*\
  !*** ./src/router.js ***!
  \***********************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var vue_router__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! vue-router */ \"./node_modules/vue-router/dist/vue-router.mjs\");\n/* harmony import */ var _apps_BuyerPage_vue__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./apps/BuyerPage.vue */ \"./src/apps/BuyerPage.vue\");\n/* harmony import */ var _apps_SellerPage_vue__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./apps/SellerPage.vue */ \"./src/apps/SellerPage.vue\");\n/* harmony import */ var _apps_About_vue__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./apps/About.vue */ \"./src/apps/About.vue\");\n\n\n\n\nconst routes = [{\n  path: '/buyer',\n  component: _apps_BuyerPage_vue__WEBPACK_IMPORTED_MODULE_0__[\"default\"]\n}, {\n  path: '/seller',\n  component: _apps_SellerPage_vue__WEBPACK_IMPORTED_MODULE_1__[\"default\"]\n}, {\n  path: '/about',\n  name: 'About',\n  // route level code-splitting\n  // this generates a separate chunk (about.[hash].js) for this route\n  // which is lazy-loaded when the route is visited.\n  component: () => Promise.resolve().then(function webpackMissingModule() { var e = new Error(\"Cannot find module '../views/About.vue'\"); e.code = 'MODULE_NOT_FOUND'; throw e; })\n}];\nconst router = (0,vue_router__WEBPACK_IMPORTED_MODULE_3__.createRouter)({\n  history: (0,vue_router__WEBPACK_IMPORTED_MODULE_3__.createWebHistory)(),\n  routes: routes\n});\n/* harmony default export */ __webpack_exports__[\"default\"] = (router);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcm91dGVyLmpzLmpzIiwibWFwcGluZ3MiOiI7Ozs7O0FBQUE7QUFFQTtBQUNBO0FBQ0E7QUFHQTtBQUVBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBR0E7QUFDQTtBQUNBO0FBQ0E7QUFFQSIsInNvdXJjZXMiOlsid2VicGFjazovL3Z1ZS10aWNrZXRzd2FwLy4vc3JjL3JvdXRlci5qcz80YzgzIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCB7IGNyZWF0ZVdlYkhpc3RvcnksIGNyZWF0ZVJvdXRlciB9IGZyb20gXCJ2dWUtcm91dGVyXCI7XG5cbmltcG9ydCBCdXllclBhZ2UgZnJvbSBcIi4vYXBwcy9CdXllclBhZ2UudnVlXCJcbmltcG9ydCBTZWxsZXJQYWdlIGZyb20gXCIuL2FwcHMvU2VsbGVyUGFnZS52dWVcIlxuaW1wb3J0IEFib3V0IGZyb20gXCIuL2FwcHMvQWJvdXQudnVlXCJcblxuXG5jb25zdCByb3V0ZXMgPSBbXG4gICAge1xuICAgICAgICBwYXRoOiAnL2J1eWVyJyxcbiAgICAgICAgY29tcG9uZW50OiBCdXllclBhZ2VcbiAgICB9LFxuICAgIHtcbiAgICAgICAgcGF0aDogJy9zZWxsZXInLFxuICAgICAgICBjb21wb25lbnQ6IFNlbGxlclBhZ2VcbiAgICB9LFxuICAgIHtcbiAgICAgICAgcGF0aDogJy9hYm91dCcsXG4gICAgICAgIG5hbWU6ICdBYm91dCcsXG4gICAgICAgIC8vIHJvdXRlIGxldmVsIGNvZGUtc3BsaXR0aW5nXG4gICAgICAgIC8vIHRoaXMgZ2VuZXJhdGVzIGEgc2VwYXJhdGUgY2h1bmsgKGFib3V0LltoYXNoXS5qcykgZm9yIHRoaXMgcm91dGVcbiAgICAgICAgLy8gd2hpY2ggaXMgbGF6eS1sb2FkZWQgd2hlbiB0aGUgcm91dGUgaXMgdmlzaXRlZC5cbiAgICAgICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJhYm91dFwiICovICcuLi92aWV3cy9BYm91dC52dWUnKVxuICAgICAgfSxcbl07XG5cbmNvbnN0IHJvdXRlciA9IGNyZWF0ZVJvdXRlcih7XG4gICAgaGlzdG9yeTogY3JlYXRlV2ViSGlzdG9yeSgpLFxuICAgIHJvdXRlczogcm91dGVzLFxufSk7XG5cbmV4cG9ydCBkZWZhdWx0IHJvdXRlcjsiXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./src/router.js\n");

/***/ })

},
/******/ function(__webpack_require__) { // webpackRuntimeModules
/******/ /* webpack/runtime/getFullHash */
/******/ !function() {
/******/ 	__webpack_require__.h = function() { return "918330b035d239c7"; }
/******/ }();
/******/ 
/******/ }
);