/** Wraps each <table> in <div class="table-wrap"> so wide tables scroll on small screens. */
export default function rehypeWrapTables() {
  return (tree) => {
    const walk = (node) => {
      if (!Array.isArray(node.children)) return;
      node.children = node.children.map((child) => {
        if (child.type === 'element' && child.tagName === 'table') {
          return { type: 'element', tagName: 'div', properties: { className: ['table-wrap'] }, children: [child] };
        }
        walk(child);
        return child;
      });
    };
    walk(tree);
  };
}
