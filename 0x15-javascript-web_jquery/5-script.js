$(function () {
  $('DIV#add_item').click(function () {
    const item = '<li>Item</>';
    $('UL.my_list').append(item);
  });
});
