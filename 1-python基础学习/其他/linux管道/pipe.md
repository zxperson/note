###1.管道

管道是进程间通信的主要手段之一。一个管道实际上就是个只存在于内存中的文件，对这个文件的操作要通过两个已经打开文件进行，它们分别代表管道的两端。管道是一种特殊的文件，它不属于某一种文件系统，而是一种独立的文件系统，有其自己的数据结构。根据管道的适用范围将其分为：无名管道和命名管道。

###2.无名管道
主要用于父进程与子进程之间，或者两个兄弟进程之间。在linux系统中可以通过系统调用建立起一个单向的通信管道，且这种关系只能由父进程来建立。

###3.命名管道
命名管道是建立在实际的磁盘介质或文件系统（而不是只存在于内存中）上有自己名字的文件，任何进程可以在任何时间通过文件名或路径名与该文件建立联系。为了实现命名管道，引入了一种新的文件类型——FIFO文件（遵循先进先出的原则）。

实现一个命名管道实际上就是实现一个FIFO文件。命名管道一旦建立，之后它的读、写以及关闭操作都与普通管道完全相同。虽然FIFO文件的inode节点在磁盘上，但是仅是一个节点而已，文件的数据还是存在于内存缓冲页面中，和普通管道相同。

###4.管道的特点：
    1) 其本质是一个伪文件(实为内核缓冲区)
    2) 由两个文件描述符引用，一个表示读端，一个表示写端。
    3) 规定数据从管道的写端流入管道，从读端流出。
    4) 数据一旦被读走，便不在管道中存在，不可反复读取。
    5) 由于管道采用半双工通信方式。因此，数据只能在一个方向上流动。
    6) 只能在有公共祖先的进程间使用管道。

###5.管道实现机制
    管道是由内核管理的一个缓冲区，相当于我们放入内存中的一个纸条。
    管道的一端连接一个进程的输出。这个进程会向管道中放入信息。
    管道的另一端连接一个进程的输入，这个进程取出被放入管道的信息。
    一个缓冲区不需要很大一般为4K大小，它被设计成为环形的数据结构，以便管道可以被循环利用。
    当管道中没有信息的话，从管道中读取的进程会等待，直到另一端的进程放入信息。
    当管道被放满信息的时候，尝试放入信息的进程会等待，直到另一端的进程取出信息。
    当两个进程都终结的时候，管道也自动消失。

![](images/pipe.png)