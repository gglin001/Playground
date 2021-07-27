# VSCode Hide Top-Right Icons

## Shortcut

add a shortcut in `keybindings.json`

```json
{ "key": "ctrl+shift+i", "command": "workbench.action.toggleDevTools" }
```

## Hide

push `ctrl+shift+i`, run below in console

```javascript
[...document.querySelectorAll(".actions-container")]
  .filter(function (obj) {
    return obj.attributes.getNamedItem("aria-label");
  })
  .filter(function (obj) {
    return obj.attributes.getNamedItem("aria-label").value == "Editor actions";
  })
  .map((a) => (a.style.display = "none"));
```

## Restore

push `ctrl+shift+i`, run below in console

```javascript
[...document.querySelectorAll(".actions-container")]
  .filter(function (obj) {
    return obj.attributes.getNamedItem("aria-label");
  })
  .filter(function (obj) {
    return obj.attributes.getNamedItem("aria-label").value == "Editor actions";
  })
  .map((a) => (a.style.display = ""));
```

## Ref

inspired from

https://github.com/Microsoft/vscode/issues/46403#issuecomment-462935343
