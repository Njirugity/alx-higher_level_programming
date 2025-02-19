$(function () {
  $('DIV#add_item').click(function () {
    const item = '<li>Item</li>';
    $('UL.my_list').append(item);
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list LI:last').remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
